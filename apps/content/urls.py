from django.urls import path

from apps.content.views import ProductFeaturedAPIView, ProductDetailAPIView, ProductListAPIView, \
    SlugPageRetrieveListAPIView

urlpatterns = [
    # featured
    path('featured_videos/', ProductFeaturedAPIView.as_view(), name='product-detail-with-objects'),

    # products
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # slug-page
    path('slug-pages/<str:slug>/', SlugPageRetrieveListAPIView.as_view(), name='slug-page-detail'),
]
