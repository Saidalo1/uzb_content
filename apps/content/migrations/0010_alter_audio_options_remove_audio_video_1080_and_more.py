# Generated by Django 5.0.2 on 2024-03-01 15:05

import apps.shared.django.utils.utils
import apps.shared.django.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_alter_productstranslation_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audio',
            options={'verbose_name': 'audio', 'verbose_name_plural': 'audios'},
        ),
        migrations.RemoveField(
            model_name='audio',
            name='video_1080',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='video_480',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='video_720',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='video_original',
        ),
        migrations.AddField(
            model_name='audio',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to=apps.shared.django.utils.utils.audio_upload_path, validators=[apps.shared.django.utils.validators.AudioValidator()], verbose_name='audio'),
        ),
        migrations.AddField(
            model_name='products',
            name='video_1080',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='videos/1080p', verbose_name='video_1080'),
        ),
        migrations.AddField(
            model_name='products',
            name='video_480',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='videos/480p', verbose_name='video_480'),
        ),
        migrations.AddField(
            model_name='products',
            name='video_720',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='videos/720p', verbose_name='video_720'),
        ),
        migrations.AddField(
            model_name='products',
            name='video_original',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='video_original'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='annotation',
            field=models.TextField(blank=True, null=True, verbose_name='annotation'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='cast',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='cast'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='cinematography',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='cinematography'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='directed_by',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='directed_by'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='episode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='episode'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='original_language',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='original_language'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='original_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='original_title'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='running_time',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='running_time'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='written_by',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='written_by'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='year',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='productstranslation',
            name='youtube_link',
            field=models.URLField(blank=True, null=True, verbose_name='youtube_link'),
        ),
        migrations.AlterModelTable(
            name='audio',
            table='audio',
        ),
    ]
