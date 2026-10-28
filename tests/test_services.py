import pytest
from src.ai_personal_assistant.services import AssistantService
from src.ai_personal_assistant.models import Priority


@pytest.fixture
def service():
    return AssistantService()


def test_add_and_list_note(service):
    note = service.add_note("Hello world", tags=["test"])
    assert note.content == "Hello world"
    assert note.tags == ["test"]
    assert len(service.list_notes()) == 1


def test_add_and_complete_task(service):
    task = service.add_task("Write tests", priority=Priority.HIGH)
    assert not task.completed
    completed = service.complete_task(task.id)
    assert completed.completed is True
    assert len(service.list_tasks(completed=False)) == 0


def test_daily_brief(service):
    service.add_task("Something")
    brief = service.daily_brief()
    assert "open tasks" in brief
