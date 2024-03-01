from django.contrib.admin import register, TabularInline, ModelAdmin
from parler.admin import TranslatableAdmin

from apps.content.models import Products, Video, Languages, SlugPage
from root.settings import languages_to_create_keys


class VideoInline(TabularInline):
    model = Video
    fields = ('language', 'video_original',)
    extra = 1
    min_num = 0


@register(Products)
class ProductsAdmin(TranslatableAdmin):
    list_display = ('title',)
    inlines = (VideoInline,)
    show_full_result_count = False

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('translations')


@register(Languages)
class LanguagesAdmin(ModelAdmin):
    fields = ('label', 'language_code')
    list_display = ('label', 'language_code')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        if obj and obj in languages_to_create_keys:
            readonly_fields.extend(['language_code'])
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False if obj and obj in languages_to_create_keys else super().has_delete_permission(request, obj)


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('video_original', 'language')


@register(SlugPage)
class SlugPageAdmin(TranslatableAdmin):
    fields = ('title', 'description')
    list_display = ('title', 'slug')
