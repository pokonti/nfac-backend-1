
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.auth.models import User
from src.projects import crud
from src.projects import schemas, models


def create_project(data: schemas.ProjectCreate, db: Session, user: User) -> models.Project:
    new_project = models.Project(
        title=data.title,
        description=data.description,
        owner_id=user.id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def get_all_projects(db: Session, user: User):
    return db.query(crud.models.Project).filter_by(owner_id=user.id).all()

def get_project_by_id(project_id: int, db: Session, user: User):
    project = db.query(models.Project).filter(models.Project.id == project_id,models.Project.owner_id == user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

def update_project(project_id: int, data: schemas.ProjectUpdate, db: Session, user: User) -> models.Project:
    project = get_project_by_id(project_id, db, user)
    for field, value in data.dict(exclude_unset=True).items():
        setattr(project, field, value)
    db.commit()
    db.refresh(project)
    return project


def delete_project(project_id: int, db: Session,  user: User) -> None:
    project = get_project_by_id(project_id, db, user)
    db.delete(project)
    db.commit()

