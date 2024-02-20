from django.contrib.admin import register, TabularInline, ModelAdmin
from parler.admin import TranslatableAdmin

from apps.content.models import Products, Video, Languages, SlugPage


class VideoInline(TabularInline):
    model = Video
    fields = ('language', 'video_original',)
    extra = 1
    min_num = 1


@register(Products)
class ProductsAdmin(TranslatableAdmin):
    list_display = ('title',)
    inlines = (VideoInline,)
    show_full_result_count = False

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('translations')


@register(Languages)
class LanguagesAdmin(TranslatableAdmin):
    fields = ('title', 'language_code')
    list_display = ('title',)


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('video_original', 'language')


@register(SlugPage)
class SlugPageAdmin(TranslatableAdmin):
    fields = ('title', 'description')
    list_display = ('title', 'slug')
