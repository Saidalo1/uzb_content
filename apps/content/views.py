from django.db.models import Subquery, F, Value, OuterRef
from django.db.models.functions import JSONObject, Coalesce
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
        return Products.objects.translated(self.request.LANGUAGE_CODE).prefetch_related('translations').order_by('-created_at')


class ProductFeaturedAPIView(ListAPIView):
    serializer_class = ProductsFeaturedModelSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_language'] = self.request.LANGUAGE_CODE
        return context

    def get_queryset(self):
        return Products.objects.filter(is_featured=True).prefetch_related('translations').order_by('-created_at')[:7]


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductsModelDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_language'] = self.request.LANGUAGE_CODE
        return context

    def get_queryset(self):
        current_pk = self.kwargs.get('pk')
        current_language = self.request.LANGUAGE_CODE

        thumbnail_subquery = Products.objects.filter(
            pk=OuterRef('pk'),
            translations__language_code=current_language
        ).values('translations__thumbnail')[:1]
        # title_subquery = Products.objects.filter(
        #     pk=OuterRef('pk'),
        #     translations__language_code=current_language
        # ).values('translations__title')[:1]

        queryset = Products.objects.filter(pk=current_pk).annotate(
            previous_obj=Subquery(
                Products.objects.filter(pk__lt=current_pk).order_by('-pk').values(
                    'pk'
                ).annotate(
                    thumbnail=Coalesce(thumbnail_subquery, F('translations__thumbnail')),
                    # title=Coalesce(title_subquery, F('translations__title')),
                    obj=JSONObject(
                        id=F('pk'),
                        thumbnail=F('thumbnail'),
                        # title=F('title')
                    )
                ).values('obj')[:1]
            ),
            next_obj=Subquery(
                Products.objects.filter(pk__gt=current_pk).order_by('pk').values(
                    'pk'
                ).annotate(
                    thumbnail=Coalesce(thumbnail_subquery, F('translations__thumbnail')),
                    # title=Coalesce(title_subquery, F('translations__title')),
                    obj=JSONObject(
                        id=F('pk'),
                        thumbnail=F('thumbnail'),
                        # title=F('title')
                    )
                ).values('obj')[:1]
            )
        ).prefetch_related('translations')

        return queryset


class SlugPageRetrieveListAPIView(RetrieveAPIView):
    queryset = SlugPage.objects.prefetch_related('translations')
    serializer_class = SlugModelDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
