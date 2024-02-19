# Origins
CSRF_TRUSTED_ORIGINS = ('http://172.23.0.1:8001',)

# Celery results
CELERY_RESULT_BACKEND = 'django-db'

# qualities of video
qualities = {
    # '240p': {'width': 426, 'height': 240},
    '480p': {'width': 854, 'height': 480},
    '720p': {'width': 1280, 'height': 720},
    '1080p': {'width': 1920, 'height': 1080}
}

# Debug toolbar
INTERNAL_IPS = [
    "127.0.0.1", "localhost"
]
