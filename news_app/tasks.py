import logging

from .celery import celery_app
from .models import News


@celery_app.task(bind=True, default_retry_delay=10 * 60)
def create_new_news(self, name, content):
    try:
        new_news = News(name=name, content=content)
        new_news.save()
        logging.info("Success")
    except Exception as e:
        logging.warning(e)
