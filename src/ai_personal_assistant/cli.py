import typer
from rich.console import Console
from rich.table import Table

from .services import AssistantService
from .models import Priority

app = typer.Typer(help="AI Personal Assistant CLI")
note_app = typer.Typer(help="Manage notes")
task_app = typer.Typer(help="Manage tasks")
app.add_typer(note_app, name="note")
app.add_typer(task_app, name="task")

service = AssistantService()
console = Console()


@note_app.command("add")
def add_note(content: str, tags: str = typer.Option("", help="Comma-separated tags")):
    """Add a new note."""
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    note = service.add_note(content, tag_list)
    console.print(f"[green]Note added[/green] (id: {note.id})")
    if note.summary:
        console.print(f"Summary: {note.summary}")


@note_app.command("list")
def list_notes():
    """List all notes."""
    notes = service.list_notes()
    if not notes:
        console.print("[yellow]No notes yet.[/yellow]")
        return
    table = Table(title="Notes")
    table.add_column("ID")
    table.add_column("Content")
    table.add_column("Summary")
    for n in notes:
        table.add_row(n.id, n.content[:50] + "..." if len(n.content) > 50 else n.content, n.summary or "-")
    console.print(table)


@task_app.command("add")
def add_task(title: str, description: str = "", priority: str = "medium"):
    """Add a new task."""
    try:
        prio = Priority(priority.lower())
    except ValueError:
        prio = Priority.MEDIUM
    task = service.add_task(title, description or None, prio)
    console.print(f"[green]Task added[/green] (id: {task.id}, priority: {task.priority.value})")


@task_app.command("list")
def list_tasks(show_completed: bool = False):
    """List tasks."""
    tasks = service.list_tasks(completed=None if show_completed else False)
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    table = Table(title="Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Priority")
    table.add_column("Done")
    for t in tasks:
        table.add_row(t.id, t.title, t.priority.value, "✓" if t.completed else "")
    console.print(table)


@task_app.command("done")
def complete_task(task_id: str):
    """Mark a task as complete."""
    task = service.complete_task(task_id)
    if task:
        console.print(f"[green]Completed:[/green] {task.title}")
    else:
        console.print("[red]Task not found.[/red]")


@app.command()
def brief():
    """Get your daily brief."""
    console.print(service.daily_brief())


if __name__ == "__main__":
    app()
