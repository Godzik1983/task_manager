"""Service layer for tasks business logic."""

from src.modules.tasks.data import Task, TaskCreate, TaskUpdate
from src.modules.tasks.repository import TasksRepository


class TasksService:
    def __init__(self, repository: TasksRepository) -> None:
        self.repository = repository

    def list_tasks(self) -> list[Task]:
        return self.repository.list_tasks()

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get_task(task_id)
        if task is None:
            raise KeyError(f"Task {task_id} not found")
        return task

    def create_task(self, payload: TaskCreate) -> Task:
        cleaned_title = payload.title.strip()
        if not cleaned_title:
            raise ValueError("Task title must not be empty")
        normalized = payload.model_copy(update={"title": cleaned_title})
        return self.repository.create_task(normalized)

    def update_task(self, task_id: int, payload: TaskUpdate) -> Task:
        updates = payload
        if payload.title is not None:
            cleaned_title = payload.title.strip()
            if not cleaned_title:
                raise ValueError("Task title must not be empty")
            updates = payload.model_copy(update={"title": cleaned_title})

        task = self.repository.update_task(task_id, updates)
        if task is None:
            raise KeyError(f"Task {task_id} not found")
        return task

    def delete_task(self, task_id: int) -> None:
        deleted = self.repository.delete_task(task_id)
        if not deleted:
            raise KeyError(f"Task {task_id} not found")
