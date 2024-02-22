from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg.openapi import Info, License, Contact
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from apps.shared.django import BothHttpAndHttpsSchemaGenerator
from root.settings import DEBUG, STATIC_ROOT, MEDIA_ROOT

schema_view = get_schema_view(
    Info(
        title="UZB Content API",
        default_version='v1',
        description="Uzbekistan Content Back-End",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=Contact(email="contact@snippets.local"),
        license=License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=[AllowAny]
)

urlpatterns = i18n_patterns(
    # Admin panel
    path('admin/', admin.site.urls),

    # apps urls
    path('', include('apps.content.urls'), name='content'),

    # Debug toolbar urls
    path("__debug__/", include("debug_toolbar.urls")),

    # CKEditor 5 urls
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

    # i18n
    path("i18n/", include("django.conf.urls.i18n")),

    # Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
)

# Static and Media URLs if DEBUG is enabled
if DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    ]
