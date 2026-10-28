from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Note(BaseModel):
    id: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    tags: list[str] = Field(default_factory=list)
    summary: Optional[str] = None


class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.MEDIUM
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    due_date: Optional[datetime] = None
