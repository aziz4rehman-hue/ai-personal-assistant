import uuid
from datetime import datetime
from typing import Optional

from .models import Note, Task, Priority


class AssistantService:
    """Core service for notes, tasks, and AI-powered insights.
    
    In-memory storage for the starter. Replace with a database (SQLite, Postgres, etc.)
    for production use.
    """

    def __init__(self):
        self.notes: dict[str, Note] = {}
        self.tasks: dict[str, Task] = {}

    # --- Notes ---
    def add_note(self, content: str, tags: Optional[list[str]] = None) -> Note:
        note_id = str(uuid.uuid4())[:8]
        note = Note(id=note_id, content=content, tags=tags or [])
        # Stub: AI summary
        note.summary = self._generate_summary(content)
        self.notes[note_id] = note
        return note

    def list_notes(self) -> list[Note]:
        return list(self.notes.values())

    # --- Tasks ---
    def add_task(self, title: str, description: Optional[str] = None, priority: Priority = Priority.MEDIUM) -> Task:
        task_id = str(uuid.uuid4())[:8]
        task = Task(id=task_id, title=title, description=description, priority=priority)
        self.tasks[task_id] = task
        return task

    def list_tasks(self, completed: Optional[bool] = None) -> list[Task]:
        tasks = list(self.tasks.values())
        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]
        return sorted(tasks, key=lambda t: (t.priority.value, t.created_at))

    def complete_task(self, task_id: str) -> Optional[Task]:
        task = self.tasks.get(task_id)
        if task:
            task.completed = True
        return task

    # --- AI Stubs (replace with real LLM calls) ---
    def _generate_summary(self, text: str) -> str:
        """Placeholder for LLM summarization."""
        words = text.split()
        if len(words) <= 10:
            return text
        return " ".join(words[:8]) + "... (AI summary stub)"

    def prioritize_tasks(self) -> list[Task]:
        """Stub for AI-powered prioritization."""
        return self.list_tasks(completed=False)

    def daily_brief(self) -> str:
        """Generate a daily brief from notes and tasks."""
        open_tasks = len(self.list_tasks(completed=False))
        recent_notes = len([n for n in self.notes.values() if (datetime.utcnow() - n.created_at).days < 1])
        return f"Daily Brief: {open_tasks} open tasks, {recent_notes} notes today. Stay focused!"
