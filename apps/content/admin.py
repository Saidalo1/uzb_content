from django.contrib.admin import register, TabularInline, ModelAdmin
from django.forms import BaseInlineFormSet
from django.utils.translation import gettext as _
from parler.admin import TranslatableAdmin

from apps.content.models import Products, Audio, Languages, SlugPage
from root.settings import languages_to_create_keys


class AudioInlineFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['language'].required = True


class AudioInline(TabularInline):
    model = Audio
    fields = ('language', 'audio',)
    extra = 1
    min_num = 0
    formset = AudioInlineFormset



@register(Products)
class ProductsAdmin(TranslatableAdmin):
    fieldsets = (
        (_('General'), {
            'fields': (
                'original_title', 'country', 'year', 'genre', 'episode', 'running_time', 'original_language',
                'directed_by', 'cinematography', 'written_by', 'cast', 'annotation', 'title', 'youtube_link',
                'is_featured', 'production', 'producer', 'thumbnail', 'video_original')}),
    )
    list_display = ('any_title',)
    inlines = (AudioInline,)
    show_full_result_count = False

    def any_title(self, obj):
        return str(obj)

    any_title.short_description = _('title')
    any_title.admin_order_field = 'translations__title'

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


@register(Audio)
class VideoAdmin(ModelAdmin):
    list_display = ('audio', 'language')


@register(SlugPage)
class SlugPageAdmin(TranslatableAdmin):
    fields = ('title', 'description', 'slug')
    list_display = ('title', 'slug')
