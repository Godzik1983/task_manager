# codex-task-manager

[![Tests](https://github.com/Godzik1983/task_manager/actions/workflows/tests.yml/badge.svg)](https://github.com/Godzik1983/task_manager/actions/workflows/tests.yml)
[![Deploy](https://github.com/Godzik1983/task_manager/actions/workflows/deploy.yml/badge.svg)](https://github.com/Godzik1983/task_manager/actions/workflows/deploy.yml)

## Project Structure

```text
codex-task-manager/
├── .github/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── error_middleware.py
│   └── modules/
│       ├── __init__.py
│       ├── README.md
│       ├── tasks/
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── controller.py
│       │   ├── service.py
│       │   ├── repository.py
│       │   ├── data.py
│       │   └── tests/
│       │       ├── __init__.py
│       │       └── test_tasks_module.py
│       ├── users/
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── controller.py
│       │   ├── service.py
│       │   ├── repository.py
│       │   ├── data.py
│       │   └── tests/
│       │       ├── __init__.py
│       │       └── test_users_module.py
│       └── auth/
│           ├── __init__.py
│           ├── router.py
│           ├── controller.py
│           ├── service.py
│           ├── repository.py
│           ├── data.py
│           └── tests/
│               ├── __init__.py
│               └── test_auth_module.py
├── tests/
│   ├── unit/
│   │   └── test_tasks_service.py
│   └── integration/
│       └── test_tasks_router.py
├── AGENTS.md
├── ARCHITECTURE.md
├── CONTROL_FLOW.md
├── SKILLS.md
├── TESTING.md
├── pytest.ini
└── requirements.txt
```

## Run

```powershell
venv\Scripts\python -m pip install -r requirements.txt
venv\Scripts\python -m uvicorn src.app:app --reload
```

## Tests

```powershell
venv\Scripts\python -m pytest -q
```

## CI/CD

### CI

- Workflow: `.github/workflows/tests.yml`
- Jobs:
  - `pytest` - запускает тесты.
  - `ruff` - запускает линт.

### CD

- Workflow: `.github/workflows/deploy.yml`
- Что делает:
  1. Собирает Docker image из `Dockerfile`.
  2. Пушит image в GHCR (`ghcr.io/<owner>/task_manager`).
  3. Подключается к VPS по SSH.
  4. Выполняет `docker compose pull && docker compose up -d`.

### Required GitHub Secrets

- `VPS_HOST` - IP/домен VPS.
- `VPS_PORT` - SSH порт (обычно `22`).
- `VPS_USER` - SSH пользователь.
- `VPS_SSH_KEY` - приватный SSH ключ для входа на VPS.
- `VPS_APP_DIR` - директория приложения на VPS (например `/opt/task_manager`).
- `VPS_REGISTRY_USER` - логин в GHCR.
- `VPS_REGISTRY_TOKEN` - токен с правом чтения пакетов GHCR (`read:packages`).
