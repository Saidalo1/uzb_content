# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
#
# from apps.content.models import Languages
# from root.settings.i18n import language_codes
#
#
# @receiver(post_migrate)
# def create_languages(sender, **kwargs):
#     for lang_code, value in language_codes.items():
#         language, created = Languages.objects.get_or_create()
