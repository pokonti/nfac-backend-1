from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from src.database import Base, engine, get_db
from sqlalchemy.orm import Session
from src.projects.router import router as project_router
from src.auth.router import router as auth_router
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
