from django.db.models import F
from rest_framework.serializers import ModelSerializer

from apps.content.models import Products
from apps.shared.django.models import TranslatedSerializerMixin


class ProductsModelListSerializer(ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context['request']
        representation['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title')


class ProductsModelDetailSerializer(ModelSerializer):
    def to_representation(self, instance):
        request = self.context['request']
        representation = super().to_representation(instance)

        representation['video_urls'] = instance.video.values(
            lang=F('language__language_code'),
            video_480p=F('video_480'),
            video_720p=F('video_720'),
            video_1080p=F('video_1080')
        )
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
