"""Repository layer for tasks."""

from src.modules.tasks.data import Task, TaskCreate, TaskUpdate


class TasksRepository:
    def __init__(self) -> None:
        self._items: dict[int, Task] = {}
        self._next_id = 1

    def list_tasks(self) -> list[Task]:
        return list(self._items.values())

    def get_task(self, task_id: int) -> Task | None:
        return self._items.get(task_id)

    def create_task(self, payload: TaskCreate) -> Task:
        task = Task(id=self._next_id, **payload.model_dump())
        self._items[self._next_id] = task
        self._next_id += 1
        return task

    def update_task(self, task_id: int, payload: TaskUpdate) -> Task | None:
        current = self._items.get(task_id)
        if current is None:
            return None

        updates = payload.model_dump(exclude_unset=True)
        updated = current.model_copy(update=updates)
        self._items[task_id] = updated
        return updated

    def delete_task(self, task_id: int) -> bool:
        if task_id not in self._items:
            return False
        del self._items[task_id]
        return True
