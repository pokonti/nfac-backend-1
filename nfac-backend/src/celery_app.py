from celery import Celery
import os

REDIS_BROKER_URL = os.getenv("REDIS_BROKER_URL", "redis://redis:6379/0")

celery = Celery(
    "worker",
    broker=REDIS_BROKER_URL,
    backend=REDIS_BROKER_URL
)

celery.conf.task_routes = {
    "src.tasks.transcribe_audio": {"queue": "audio"}
}
celery.autodiscover_tasks(['src'])