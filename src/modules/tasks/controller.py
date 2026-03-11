"""Controller layer for tasks."""

from src.modules.tasks.data import Task, TaskCreate, TaskUpdate
from src.modules.tasks.service import TasksService


class TasksController:
    def __init__(self, service: TasksService) -> None:
        self.service = service

    def list_tasks(self) -> list[Task]:
        return self.service.list_tasks()

    def get_task(self, task_id: int) -> Task:
        return self.service.get_task(task_id)

    def create_task(self, payload: TaskCreate) -> Task:
        return self.service.create_task(payload)

    def update_task(self, task_id: int, payload: TaskUpdate) -> Task:
        return self.service.update_task(task_id, payload)

    def delete_task(self, task_id: int) -> None:
        self.service.delete_task(task_id)
