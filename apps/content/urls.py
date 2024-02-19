from django.urls import path

from apps.content.views import VideoRetrieveAPIView, ProductDetailAPIView, ProductListAPIView, \
    ProductWithObjectsRetrieveAPIView

urlpatterns = [
    # products
    path('products/', ProductListAPIView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('product/<int:pk>/<int:count>/', ProductWithObjectsRetrieveAPIView.as_view(),
         name='product-detail-with-objects'),

    # videos
    path('videos/<int:pk>/<int:quality>/', VideoRetrieveAPIView.as_view(), name='video-detail')
]
