from os import environ

from celery import Celery

environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
app = Celery("root")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = True
