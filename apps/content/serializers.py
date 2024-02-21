from django.db.models import Q
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework.serializers import ModelSerializer

from apps.content.models import Products, SlugPage
from apps.shared.django.models import TranslatedSerializerMixin


class ProductsModelListSerializer(ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context['request']
        representation['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title', 'annotation')


class ProductsModelDetailSerializer(ModelSerializer):
    def to_representation(self, instance):
        request = self.context['request']
        representation = super().to_representation(instance)

        video_urls = {}

        for video in instance.video.exclude(
                Q(video_480__isnull=True) | Q(video_480__exact=''),
                Q(video_720__isnull=True) | Q(video_720__exact=''),
                Q(video_1080__isnull=True) | Q(video_1080__exact='')
        ):
            lang_code = video.language.language_code
            video_data = {}

            if video.video_480:
                video_data["video_480"] = request.build_absolute_uri(video.video_480.url)
            if video.video_720:
                video_data["video_720"] = request.build_absolute_uri(video.video_720.url)
            if video.video_1080:
                video_data["video_1080"] = request.build_absolute_uri(video.video_1080.url)

            if lang_code in video_urls:
                video_urls[lang_code].update(video_data)
            else:
                video_urls[lang_code] = video_data

        representation['video_urls'] = video_urls
        representation['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title', 'annotation', "youtube_link", "year", "country", "genre", "episode",
                  "original_title", "running_time", "original_language", "directed_by", "written_by", "cinematography",
                  "cast")


class ProductsFeaturedModelSerializer(ModelSerializer, TranslatedSerializerMixin):

    def to_representation(self, instance):
        request = self.context['request']
        representation = super().to_representation(instance)

        representation['video_url'] = request.build_absolute_uri(instance.video.first().video_720.url)
        representation['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title', 'annotation')


class SlugModelDetailSerializer(TranslatableModelSerializer):
    class Meta:
        model = SlugPage
        fields = ('id', 'title', 'description')
