
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from src.auth.models import User
from src.auth.service import get_current_user
from src.database import get_db
from src.projects import schemas, crud

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

@router.get("/", response_model=list[schemas.Project])
def read_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_all_projects(db, current_user)


@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_project(project, db, current_user)


@router.get("/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = crud.get_project_by_id(project_id, db, current_user)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.patch("/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, data: schemas.ProjectUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = crud.get_project_by_id(project_id, db, current_user)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.update_project(project_id, data, db)


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = crud.get_project_by_id(project_id, db, current_user)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    crud.delete_project(project_id, db, current_user)
    return {"message": "Project deleted"}