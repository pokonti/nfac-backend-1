from fastapi import FastAPI, UploadFile, File, Depends
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from src.database import Base, engine, get_db
from sqlalchemy.orm import Session
from src.projects.router import router as project_router
from src.auth.router import router as auth_router
from src.assistant.api import router as assistant_router
from tempfile import NamedTemporaryFile
from celery.result import AsyncResult
from src.tasks import transcribe_audio
from src.celery_app import celery
import os
app = FastAPI()
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]
origins = [
    "http://localhost:5173",
    "https://crypto-frontend-cly7.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(project_router)
app.include_router(auth_router)
app.include_router(assistant_router)

# @app.post("/whisper/")
# async def upload_mp3(file: UploadFile = File(...)):
#     with NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
#         tmp.write(await file.read())
#         tmp_path = tmp.name
#
#     task = transcribe_audio.delay(tmp_path)
#     return {"task_id": task.id}
UPLOAD_DIR = "/app/shared"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/whisper/")
async def upload_audio(file: UploadFile = File(...)):
    suffix = "." + file.filename.split(".")[-1]
    with NamedTemporaryFile(delete=False, suffix=suffix, dir=UPLOAD_DIR) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    task = transcribe_audio.delay(tmp_path)
    return {"task_id": task.id}

@app.get("/result/{task_id}")
def get_transcription(task_id: str):
    result = AsyncResult(task_id, app=celery)
    return {
        "status": result.status,
        "result": result.result if result.ready() else None
    }
