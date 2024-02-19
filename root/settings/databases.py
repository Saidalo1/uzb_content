from root.settings.default_settings import env

DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE'),
        'NAME': env('SQL_NAME'),
        'USER': env('SQL_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('SQL_HOST'),
        'PORT': env('SQL_PORT')
    }
}
