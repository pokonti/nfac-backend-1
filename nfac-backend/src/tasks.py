from src.celery_app import celery
from src.whisper_utils import transcribe

@celery.task(name="src.tasks.transcribe_audio")
def transcribe_audio(file_path: str):
    return transcribe(file_path)
