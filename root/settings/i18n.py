# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
from os.path import join

from django.utils.translation import gettext_lazy as _

from root.settings import BASE_DIR, env

# from django.conf.global_settings import LANGUAGES

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = [('ru', _('Russian')), ('uz', _('Uzbek'))]

# Path to save locale files
LOCALE_PATHS = [
    join(BASE_DIR, env.str('TRANSLATES_PATH', 'locale'))
]

# Django Parler Settings
PARLER_LANGUAGES = {
    None: [
        {'code': language[0]} for language in LANGUAGES
    ],
    'default': {
        'fallback': LANGUAGE_CODE,
        'hide_untranslated': True,
    }
}
