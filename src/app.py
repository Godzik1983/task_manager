"""Application entrypoint."""

from fastapi import FastAPI

from src.middleware.error_middleware import ErrorMiddleware
from src.modules.tasks.router import router as tasks_router

app = FastAPI(title="Codex Task Manager")
app.add_middleware(ErrorMiddleware)
app.include_router(tasks_router)


@app.get("/health", tags=["system"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
