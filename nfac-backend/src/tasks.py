from celery_worker import celery
from .whisper_utils import transcribe

@celery.task(name="src.tasks.transcribe_audio")
def transcribe_audio(file_path: str):
    return transcribe(file_path)
