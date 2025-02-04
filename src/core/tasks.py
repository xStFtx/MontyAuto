from celery import Celery
from src.core.config import settings

app = Celery(
    'automation',
    broker=settings.redis_url,
    backend=settings.redis_url,
    include=['src.modules.trading.tasks']
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1
) 