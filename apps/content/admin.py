from django.contrib.admin import register, TabularInline, ModelAdmin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin

from apps.content.models import Products, Video, Languages


class VideoInline(TabularInline):
    model = Video
    fields = ('language', 'video_original', 'thumbnail', 'is_active')
    extra = 1
    min_num = 1


@register(Products)
class ProductsAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (_('Metadata'), {
            'fields': ('title', 'annotation', 'is_featured', 'year', 'country', 'genre', 'episode', 'original_title',
                       'running_time', 'original_language')
        }),
        (_('Creators'), {
            'fields': ('directed_by', 'written_by', 'cinematography')
        }),
        (_('Actors'), {
            'fields': ('cast',)
        }),
        (_('Availability'), {
            'fields': ('youtube_link', 'is_active')
        })
    )
    inlines = (VideoInline,)
    show_full_result_count = False

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('translations')


@register(Languages)
class LanguagesAdmin(TranslatableAdmin):
    fields = ('title', 'language_code', 'is_active')
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)


@register(Video)
class VideoAdmin(ModelAdmin):
    fieldsets = (
        (_('Personal Information'), {
            'fields': ('video_original', 'product', 'thumbnail')
        }),
        (_('Details'), {
            'fields': ('is_active', 'language')
        }),
    )
