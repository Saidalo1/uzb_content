MIDDLEWARE = [
    # Django default middlewares
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Debug toolbar middleware
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # MultiLanguageMiddleware
    'django.middleware.locale.LocaleMiddleware',
    'apps.shared.django.middlewares.CustomLocaleMiddleware'
]
