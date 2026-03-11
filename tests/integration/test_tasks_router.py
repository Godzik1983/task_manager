from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.modules.tasks.controller import TasksController
from src.modules.tasks.repository import TasksRepository
from src.modules.tasks.router import get_tasks_controller, router
from src.modules.tasks.service import TasksService


def build_client() -> TestClient:
    app = FastAPI()
    app.include_router(router)

    controller = TasksController(TasksService(TasksRepository()))
    app.dependency_overrides[get_tasks_controller] = lambda: controller

    return TestClient(app)


def test_router_crud_flow() -> None:
    client = build_client()

    create_response = client.post("/tasks", json={"title": "Write tests", "description": "Unit + integration"})
    assert create_response.status_code == 201
    created = create_response.json()
    task_id = created["id"]
    assert created["title"] == "Write tests"

    list_response = client.get("/tasks")
    assert list_response.status_code == 200
    items = list_response.json()
    assert len(items) == 1
    assert items[0]["id"] == task_id

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Write tests"

    update_response = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert update_response.status_code == 200
    assert update_response.json()["completed"] is True

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    not_found_response = client.get(f"/tasks/{task_id}")
    assert not_found_response.status_code == 404


def test_router_returns_404_for_missing_task() -> None:
    client = build_client()

    assert client.get("/tasks/999").status_code == 404
    assert client.patch("/tasks/999", json={"completed": True}).status_code == 404
    assert client.delete("/tasks/999").status_code == 404


def test_router_returns_400_for_invalid_title_on_create() -> None:
    client = build_client()

    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 400


def test_router_returns_400_for_invalid_title_on_update() -> None:
    client = build_client()

    create_response = client.post("/tasks", json={"title": "task"})
    task_id = create_response.json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={"title": "   "})
    assert response.status_code == 400
