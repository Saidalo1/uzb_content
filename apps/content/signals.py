from django.db.models.signals import post_migrate
from django.dispatch import receiver

from apps.content.models import Languages
from root.settings import languages_to_create


@receiver(post_migrate)
def create_languages(sender, **kwargs):
    for language_data in languages_to_create:
        try:
            Languages.objects.get_or_create(**language_data)
        except:
            pass
