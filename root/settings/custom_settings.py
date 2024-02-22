# Origins
import socket

# Django Core
CSRF_TRUSTED_ORIGINS = ['https://cp.uzbcontent.com', 'https://uzbcontent.com', 'http://172.23.0.1:8888',
                        'https://*.uzbcontent.com']
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", 'https://uzbcontent.com', 'https://cp.uzbcontent.com']

# Celery results
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_EXTENDED = True

# qualities of video
qualities = {
    # '240p': {'width': 426, 'height': 240},
    '480p': {'width': 854, 'height': 480},
    '720p': {'width': 1280, 'height': 720},
    '1080p': {'width': 1920, 'height': 1080}
}

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "localhost", "172.23.0.1"]

languages_to_create = {'uz': "O'zbek", 'ru': "Русский язык", 'en': "English"}
languages_to_create_keys = languages_to_create.keys()

# Django Media https
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
