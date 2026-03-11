# codex-task-manager

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
