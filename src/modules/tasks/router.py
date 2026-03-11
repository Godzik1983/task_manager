"""FastAPI router for tasks."""

from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.modules.tasks.controller import TasksController
from src.modules.tasks.data import Task, TaskCreate, TaskUpdate
from src.modules.tasks.repository import TasksRepository
from src.modules.tasks.service import TasksService

router = APIRouter(prefix="/tasks", tags=["tasks"])

_default_controller = TasksController(TasksService(TasksRepository()))


def get_tasks_controller() -> TasksController:
    return _default_controller


@router.get("", response_model=list[Task])
def list_tasks(controller: TasksController = Depends(get_tasks_controller)) -> list[Task]:
    return controller.list_tasks()


@router.post("", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate, controller: TasksController = Depends(get_tasks_controller)
) -> Task:
    try:
        return controller.create_task(payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, controller: TasksController = Depends(get_tasks_controller)) -> Task:
    try:
        return controller.get_task(task_id)
    except KeyError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch("/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    controller: TasksController = Depends(get_tasks_controller),
) -> Task:
    try:
        return controller.update_task(task_id, payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except KeyError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, controller: TasksController = Depends(get_tasks_controller)) -> Response:
    try:
        controller.delete_task(task_id)
    except KeyError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    return Response(status_code=status.HTTP_204_NO_CONTENT)
