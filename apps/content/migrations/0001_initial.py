# Generated by Django 5.0.2 on 2024-02-21 08:59

import django.db.models.deletion
import django_ckeditor_5.fields
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=255, verbose_name='title')),
                ('language_code', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_featured', models.BooleanField(default=False, verbose_name='is_featured')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SlugPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'slug_page',
                'verbose_name_plural': 'slug_pages',
                'db_table': 'slug_page',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('annotation', models.TextField(verbose_name='annotation')),
                ('youtube_link', models.URLField(verbose_name='youtube_link')),
                ('year', models.CharField(max_length=255, verbose_name='year')),
                ('country', models.CharField(max_length=255, verbose_name='country')),
                ('genre', models.CharField(max_length=255, verbose_name='genre')),
                ('episode', models.CharField(max_length=255, verbose_name='episode')),
                ('original_title', models.CharField(max_length=255, verbose_name='original_title')),
                ('running_time', models.CharField(max_length=255, verbose_name='running_time')),
                ('original_language', models.CharField(max_length=255, verbose_name='original_language')),
                ('directed_by', models.CharField(max_length=255, verbose_name='directed_by')),
                ('written_by', models.CharField(max_length=255, verbose_name='written_by')),
                ('cinematography', models.CharField(max_length=255, verbose_name='cinematography')),
                ('cast', models.CharField(max_length=255, verbose_name='cast')),
                ('thumbnail', models.ImageField(upload_to='thumbnails/', verbose_name='thumbnail')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='content.products')),
            ],
            options={
                'verbose_name': 'product Translation',
                'db_table': 'product_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SlugPageTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(max_length=2048, verbose_name='description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='content.slugpage')),
            ],
            options={
                'verbose_name': 'slug_page Translation',
                'db_table': 'slug_page_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('video_original', models.FileField(upload_to='videos/', verbose_name='video_original')),
                ('video_480', models.FileField(blank=True, max_length=255, null=True, upload_to='videos/480p', verbose_name='video_480')),
                ('video_720', models.FileField(blank=True, max_length=255, null=True, upload_to='videos/720p', verbose_name='video_720')),
                ('video_1080', models.FileField(blank=True, max_length=255, null=True, upload_to='videos/1080p', verbose_name='video_1080')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='duration')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language', to='content.languages', verbose_name='language')),
                ('product', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video', to='content.products')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
                'db_table': 'video',
                'unique_together': {('product', 'language')},
            },
        ),
    ]
