from celery import Celery
import os

REDIS_BROKER_URL = os.getenv("REDIS_BROKER_URL")

# Create the Celery app instance
celery = Celery(
    "worker",
    broker=REDIS_BROKER_URL
)

# Optional: routing for specific tasks or queues
celery.conf.task_routes = {
    "src.tasks.transcribe_audio": {"queue": "audio"}
}
