from rest_framework.serializers import ModelSerializer

from apps.content.models import Video, Products
from root.settings import MEDIA_URL


class ProductsModelListSerializer(ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context['request']
        media = instance.media[0]
        media['thumbnail'] = request.build_absolute_uri(media.get('thumbnail')).replace(
            f"/{request.LANGUAGE_CODE}/{Products.__name__.lower()}/", f"/{MEDIA_URL}")
        media['video'] = request.build_absolute_uri(media.get('video')).replace(
            f"/{request.LANGUAGE_CODE}/{Products.__name__.lower()}/", f"/{MEDIA_URL}")
        representation['media'] = media
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title')


class ProductsModelDetailSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context['request']
        media = instance.media[0]
        media['thumbnail'] = request.build_absolute_uri(media.get('thumbnail')).replace(
            f"/{request.LANGUAGE_CODE}/{Products.__name__.lower()}/{instance.pk}/", f"/{MEDIA_URL}")
        media['video'] = request.build_absolute_uri(media.get('video')).replace(
            f"/{request.LANGUAGE_CODE}/{Products.__name__.lower()}/{instance.pk}/", f"/{MEDIA_URL}")
        representation['media'] = media
        return representation

    class Meta:
        model = Products
        fields = ('id', 'title', 'annotation', "youtube_link", "year", "country", "genre", "episode",
                  "original_title", "running_time", "original_language", "directed_by", "written_by", "cinematography",
                  "cast")


class VideoModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context['request']
        representation['video'] = request.build_absolute_uri(
            getattr(instance, f"video_{self.context['quality']}")).replace(
            f"/{request.LANGUAGE_CODE}/{Products.__name__.lower()}/{instance.pk}/", f"/{MEDIA_URL}")
        return representation

    class Meta:
        model = Video
        fields = ('id',)
