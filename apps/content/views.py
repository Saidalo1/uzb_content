from rest_framework.generics import ListAPIView

from apps.content.models import Products
from apps.content.serializers import ProductsFeaturedModelSerializer, ProductsModelDetailSerializer, \
    ProductsModelListSerializer
from apps.shared.django.utils import ProductPagination


class ProductListAPIView(ListAPIView):
    pagination_class = ProductPagination
    serializer_class = ProductsModelListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_language'] = self.request.LANGUAGE_CODE
        return context

    def get_queryset(self):
        return Products.objects.filter(is_featured=True).order_by('-created_at')


class ProductFeaturedAPIView(ListAPIView):
    serializer_class = ProductsFeaturedModelSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_language'] = self.request.LANGUAGE_CODE
        return context

    def get_queryset(self):
        return Products.objects.filter(is_featured=True).order_by('-created_at')[:7]


class ProductDetailAPIView(ListAPIView):
    serializer_class = ProductsModelDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_language'] = self.request.LANGUAGE_CODE
        return context

    def get_queryset(self):
        return Products.objects.filter(pk=self.kwargs['pk'])
