# Application definition
INSTALLED_APPS = [
    # jazzmin (admin panel)
    'jazzmin',

    # Django default applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My applications
    'apps.content.apps.ContentConfig',

    # Third-party applications
    'rest_framework',
    'drf_yasg',
    'parler',
    'corsheaders',
    'django_filters',
    'debug_toolbar',
    'django_ckeditor_5',
    'django_celery_results',
]
