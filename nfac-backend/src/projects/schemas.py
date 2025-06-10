from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Project(ProjectBase):
    id: int
    created_at: datetime

