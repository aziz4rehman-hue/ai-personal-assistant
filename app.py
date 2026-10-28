from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from src.ai_personal_assistant.services import AssistantService
from src.ai_personal_assistant.models import Priority

app = FastAPI(
    title="AI Personal Assistant",
    description="Web API for notes, tasks, and AI insights",
    version="0.1.0",
)

service = AssistantService()


class NoteCreate(BaseModel):
    content: str
    tags: list[str] = []


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"


@app.get("/")
def root():
    return {"message": "AI Personal Assistant API", "docs": "/docs"}


@app.post("/notes")
def create_note(note: NoteCreate):
    created = service.add_note(note.content, note.tags)
    return created


@app.get("/notes")
def get_notes():
    return service.list_notes()


@app.post("/tasks")
def create_task(task: TaskCreate):
    try:
        prio = Priority(task.priority.lower())
    except ValueError:
        prio = Priority.MEDIUM
    created = service.add_task(task.title, task.description, prio)
    return created


@app.get("/tasks")
def get_tasks(completed: Optional[bool] = None):
    return service.list_tasks(completed)


@app.post("/tasks/{task_id}/complete")
def complete_task(task_id: str):
    task = service.complete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.get("/brief")
def daily_brief():
    return {"brief": service.daily_brief()}
