"""
Main entrypoint for starting Celery task queue for Django
"""

import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aica_django.settings")

app = Celery("aica_django")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Discover apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  # type: ignore
app.conf.timezone = "UTC"
