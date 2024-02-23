from root.settings.ckeditor_configs import customColorPalette, CKEDITOR_5_CONFIGS
from root.settings.custom_settings import CSRF_TRUSTED_ORIGINS, CELERY_RESULT_EXTENDED, CELERY_RESULT_BACKEND, \
    qualities, INTERNAL_IPS, languages_to_create, languages_to_create_keys, CORS_ALLOWED_ORIGINS, \
    SECURE_PROXY_SSL_HEADER, USE_X_FORWARDED_HOST, DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION, \
    DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS, DJANGORESIZED_DEFAULT_FORCE_FORMAT, DJANGORESIZED_DEFAULT_KEEP_META, \
    DJANGORESIZED_DEFAULT_QUALITY, DJANGORESIZED_DEFAULT_SIZE
from root.settings.databases import DATABASES
from root.settings.default_settings import *
from root.settings.i18n import LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_TZ, PARLER_LANGUAGES, LOCALE_PATHS, LANGUAGES
from root.settings.installed_apps import INSTALLED_APPS
from root.settings.jazzmin_configs import JAZZMIN_SETTINGS
from root.settings.middlewares import MIDDLEWARE
