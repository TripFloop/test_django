import os

from celery import Celery
# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

celery_app = Celery('news_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'creating-new-news': {
        'task': 'news_app.tasks.create_new_news',
        'schedule': crontab(minute="*/5"),
        'args': {"name": "Some news", "content": "Some description"}
    }
}
