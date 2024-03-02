from django.db import IntegrityError
from django.db.models import DurationField, FileField, BooleanField, URLField, \
    ForeignKey, SET_NULL, CharField, TextField, SlugField
from django.db.transaction import on_commit
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField
from parler.models import TranslatableModel, TranslatedFields
from unidecode import unidecode

from apps.shared.django.models import TimeBaseModel
from apps.shared.django.utils.change_video_qualities import transcode_video
from apps.shared.django.utils.utils import audio_upload_path
from apps.shared.django.utils.validators import AudioValidator


class Languages(TimeBaseModel):
    label = CharField(_('title'), max_length=255)
    language_code = CharField(max_length=5, unique=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'language'
        verbose_name = _('language')
        verbose_name_plural = _('languages')


class SlugPage(TimeBaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=CharField(_('title'), max_length=255),
        description=CKEditor5Field(_('description'), max_length=2048)
    )
    slug = SlugField(_('slug'), db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('content:article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.safe_translation_getter('title', any_language=True)))
        try:
            super().save(*args, **kwargs)
            return
        except IntegrityError:
            self.slug = self._generate_unique_slug()
            super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        """
        Generate a unique slug by appending a unique number to the original slug.
        """
        original_slug = self.slug
        counter = 1
        while True:
            new_slug = f'{original_slug}-{counter}'
            if not SlugPage.objects.filter(slug=new_slug).exists():
                return new_slug
            counter += 1

    def __str__(self):
        return f"{self.safe_translation_getter('title', any_language=True)}"

    class Meta:
        db_table = 'slug_page'
        verbose_name = _('slug_page')
        verbose_name_plural = _('slug_pages')


class Products(TimeBaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=CharField(_('title'), max_length=255),
        annotation=TextField(_('annotation'), null=True, blank=True),
        youtube_link=URLField(_('youtube_link'), null=True, blank=True),
        year=CharField(_('year'), max_length=255, null=True, blank=True),
        country=CharField(_('country'), max_length=255, null=True, blank=True),
        genre=CharField(_('genre'), max_length=255, null=True, blank=True),
        episode=CharField(_('episode'), max_length=255, null=True, blank=True),
        original_title=CharField(_('original_title'), max_length=255, null=True, blank=True),
        running_time=CharField(_('running_time'), max_length=255, null=True, blank=True),
        original_language=CharField(_('original_language'), max_length=255, null=True, blank=True),
        directed_by=CharField(_('directed_by'), max_length=255, null=True, blank=True),
        written_by=CharField(_('written_by'), max_length=255, null=True, blank=True),
        cinematography=CharField(_('cinematography'), max_length=255, null=True, blank=True),
        cast=CharField(_('cast'), max_length=255, null=True, blank=True),
        production=CharField(_('production'), max_length=255, null=True, blank=True),
        # is_active=BooleanField(_('is_active'), default=True),
        # thumbnail=ImageField(_('thumbnail'), upload_to='thumbnails/'),
        thumbnail=ResizedImageField(_('thumbnail'), upload_to='thumbnails/', size=[640, 360], quality=80,
                                    force_format='WEBP', crop=['middle', 'center'], null=True, blank=True)
    )
    video_original = FileField(_('video_original'), upload_to='videos/', null=True, blank=True)
    video_480 = FileField(_('video_480'), upload_to='videos/480p', null=True, blank=True, max_length=255)
    video_720 = FileField(_('video_720'), upload_to='videos/720p', null=True, blank=True, max_length=255)
    video_1080 = FileField(_('video_1080'), upload_to='videos/1080p', null=True, blank=True, max_length=255)
    is_featured = BooleanField(_('is_featured'), default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.video_original and self.video_original.name:
            on_commit(lambda: transcode_video.delay(self.pk))

    def __str__(self):
        return f"{self.safe_translation_getter('title', any_language=True)}"

    class Meta:
        db_table = 'product'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class Audio(TimeBaseModel):
    # audio = FileField(_('audio'), upload_to=audio_upload_path, validators=[AudioValidator()], null=True, blank=True)
    audio = FileField(_('audio'), upload_to=audio_upload_path, null=True, blank=True)
    product = ForeignKey('content.Products', SET_NULL, 'audios', null=True, blank=True, max_length=255)
    duration = DurationField(_('duration'), null=True, blank=True)
    # is_active = BooleanField(_('is_active'), default=True)
    language = ForeignKey('content.Languages', SET_NULL, 'language', verbose_name=_('language'), null=True, blank=True)

    def __str__(self):
        return f"{self.audio.name} - {self.language.language_code}"

    class Meta:
        unique_together = ('product', 'language')
        db_table = 'audio'
        verbose_name = _('audio')
        verbose_name_plural = _('audios')
