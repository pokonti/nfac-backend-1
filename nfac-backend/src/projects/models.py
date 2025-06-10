from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime

from sqlalchemy.orm import relationship

from src.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="projects")

