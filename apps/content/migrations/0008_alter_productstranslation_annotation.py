# Generated by Django 5.0.2 on 2024-02-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_remove_productstranslation_is_featured_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstranslation',
            name='annotation',
            field=models.TextField(verbose_name='annotation'),
        ),
    ]
