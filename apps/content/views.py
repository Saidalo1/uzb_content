from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.content.models import Products, SlugPage
from apps.content.serializers import ProductsFeaturedModelSerializer, ProductsModelDetailSerializer, \
    ProductsModelListSerializer, SlugModelDetailSerializer
from apps.shared.django.utils import ProductPagination


class ProductListAPIView(ListAPIView):
    pagination_class = ProductPagination
    serializer_class = ProductsModelListSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'translations__title', 'translations__annotation', 'translations__original_title', 'translations__directed_by',
        'translations__written_by', 'translations__cinematography', 'translations__cast'
    )

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
        return Products.objects.filter(pk=self.kwargs.get('pk'))


class SlugPageRetrieveListAPIView(RetrieveAPIView):
    queryset = SlugPage.objects.all()
    serializer_class = SlugModelDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
