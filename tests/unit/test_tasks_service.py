import pytest

from src.modules.tasks.data import TaskCreate, TaskUpdate
from src.modules.tasks.repository import TasksRepository
from src.modules.tasks.service import TasksService


def build_service() -> TasksService:
    return TasksService(TasksRepository())


def test_service_create_and_get_task() -> None:
    service = build_service()

    created = service.create_task(TaskCreate(title="  Buy milk  ", description="2L"))

    assert created.id == 1
    assert created.title == "Buy milk"
    assert created.description == "2L"
    assert service.get_task(created.id).id == created.id


def test_service_create_task_rejects_empty_title() -> None:
    service = build_service()

    with pytest.raises(ValueError):
        service.create_task(TaskCreate(title="   "))


def test_service_update_and_delete_task() -> None:
    service = build_service()
    created = service.create_task(TaskCreate(title="Initial"))

    updated = service.update_task(created.id, TaskUpdate(title="Updated", completed=True))
    assert updated.title == "Updated"
    assert updated.completed is True

    service.delete_task(created.id)

    with pytest.raises(KeyError):
        service.get_task(created.id)


def test_service_update_missing_task_raises_key_error() -> None:
    service = build_service()

    with pytest.raises(KeyError):
        service.update_task(999, TaskUpdate(title="Ghost"))


def test_service_delete_missing_task_raises_key_error() -> None:
    service = build_service()

    with pytest.raises(KeyError):
        service.delete_task(999)
