from django.db.models import F, Value, CharField, ExpressionWrapper
from django.db.models.functions import Concat
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework.serializers import ModelSerializer

from apps.content.models import Products, SlugPage
from apps.shared.django.models import TranslatedSerializerMixin
from root.settings import MEDIA_URL


class ProductsModelListSerializer(ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context['request']
        try:
            representation['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        except ValueError:
            representation['thumbnail'] = None
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title', 'annotation')


class ProductsModelDetailSerializer(ModelSerializer):
    def to_representation(self, instance):
        request = self.context['request']
        representation = super().to_representation(instance)

        video_urls = []

        video_data = {}

        if instance.video_480:
            video_data["video_480"] = request.build_absolute_uri(instance.video_480.url)
        if instance.video_720:
            video_data["video_720"] = request.build_absolute_uri(instance.video_720.url)
        if instance.video_1080:
            video_data["video_1080"] = request.build_absolute_uri(instance.video_1080.url)
        if any(video_data.values()):
            video_data['language'] = instance.audios.annotate(
                absolute_audio_url=ExpressionWrapper(
                    Concat(Value(request.build_absolute_uri('/')), Value(MEDIA_URL), 'audio', output_field=CharField()),
                    output_field=CharField())).values('absolute_audio_url', title=F('language__label'),
                                                      code=F('language__language_code'))
        video_urls.append(video_data)

        representation['video_urls'] = video_urls if any(video_urls) else None
        try:
            representation['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        except ValueError:
            representation['thumbnail'] = None

        next_obj, previous_obj = instance.next_obj, instance.previous_obj
        base_url = request.build_absolute_uri('/')
        if next_obj is not None:
            if next_obj.get('thumbnail', '') != '':
                try:
                    next_obj['thumbnail'] = base_url + MEDIA_URL + next_obj['thumbnail']
                except ValueError:
                    next_obj['thumbnail'] = None
            else:
                next_obj['thumbnail'] = None
            representation['next_obj'] = next_obj
        if previous_obj and next_obj:
            if next_obj.get('previous', '') != '':
                try:
                    previous_obj['thumbnail'] = base_url + MEDIA_URL + previous_obj['thumbnail']
                except ValueError:
                    previous_obj['thumbnail'] = None
            else:
                previous_obj['thumbnail'] = None
            representation['previous_obj'] = previous_obj
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title', 'annotation', "youtube_link", "year", "country", "genre", "episode",
                  "original_title", "running_time", "original_language", "directed_by", "written_by", "cinematography",
                  "cast", 'production')


class ProductsFeaturedModelSerializer(ModelSerializer, TranslatedSerializerMixin):

    def to_representation(self, instance):
        request = self.context['request']
        representation = super().to_representation(instance)

        try:
            representation['video_url'] = request.build_absolute_uri(instance.video_720.url)
        except ValueError:
            representation['video_url'] = None

        if representation['video_url']:
            representation['language'] = instance.audios.annotate(
                absolute_audio_url=ExpressionWrapper(
                    Concat(Value(request.build_absolute_uri('/')), Value(MEDIA_URL), 'audio', output_field=CharField()),
                    output_field=CharField())).values('absolute_audio_url', title=F('language__label'),
                                                      code=F('language__language_code'))
        try:
            representation['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        except ValueError:
            representation['thumbnail'] = None
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title', 'annotation')


class SlugModelDetailSerializer(TranslatableModelSerializer):
    class Meta:
        model = SlugPage
        fields = ('id', 'title', 'description')
