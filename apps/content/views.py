from django.contrib.postgres.expressions import ArraySubquery
from django.db.models import OuterRef, Subquery
from django.db.models.functions import JSONObject
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.content.models import Video, Products
from apps.content.serializers import VideoModelSerializer, ProductsModelDetailSerializer, ProductsModelListSerializer
from apps.shared.django.utils import ProductPagination
from root.settings import qualities


class ProductBaseModelView:
    def get_queryset(self):
        current_language = self.request.LANGUAGE_CODE
        sub_query = Subquery(
            Video.objects.filter(product_id=OuterRef('id'), language__language_code=current_language).values(
                json=JSONObject(id="id", thumbnail="thumbnail", video="video_original")).filter(thumbnail__isnull=False,
                                                                                                video_original__isnull=False)[
            :1])
        return Products.objects.translated(language_code=current_language).annotate(
            media=ArraySubquery(sub_query)).filter(media__isnull=False).prefetch_related('translations')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ProductListAPIView(ProductBaseModelView, ListAPIView):
    serializer_class = ProductsModelListSerializer
    pagination_class = ProductPagination


class ProductDetailAPIView(ProductBaseModelView, RetrieveAPIView):
    serializer_class = ProductsModelDetailSerializer


class VideoRetrieveAPIView(RetrieveAPIView):
    serializer_class = VideoModelSerializer

    def get(self, request, *args, **kwargs):
        if f"{kwargs.get('quality')}p" not in qualities.keys():
            return Response({"error": _("Invalid quality parameter")}, HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        context['quality'] = self.kwargs.get('quality')
        return context

    def get_queryset(self):
        return Video.objects.filter(pk=self.kwargs.get('pk'), language__language_code=self.request.LANGUAGE_CODE)


class ProductWithObjectsRetrieveAPIView(ProductBaseModelView, RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsModelDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context['request'] = self.request

        return context

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        selected_products = self.get_queryset().exclude(pk=instance.pk).filter(translations__is_featured=True)[
                            :self.kwargs.get('count')]

        selected_products_serializer = ProductsModelListSerializer(selected_products, context={'request': self.request},
                                                                   many=True)

        serializer = self.get_serializer(self.get_queryset().filter(pk=instance.pk), context={'request': self.request},
                                         many=True)

        return Response(serializer.data + selected_products_serializer.data)
