Отлично, теперь понятно, что ты хочешь 👍
Тебе **не нужен готовый код**, тебе нужно **настроить Codex-агента в IDE**, чтобы он сам:

* создавал структуру проекта
* генерировал код
* писал тесты
* исправлял баги
* обновлял архитектуру
* коммитил в GitHub

То есть фактически сделать **Codex-driven development workflow**.

Ниже я дам **реальную структуру инструкций для Codex**:
`AGENTS.md`, `SKILLS.md`, `CONTROL_FLOW.md`, `ARCHITECTURE.md`, `TESTING.md` + **команды для Codex**.

Все это позволит в VS Code писать примерно такие команды:

```
/agent create-project
/agent generate-router tasks
/agent generate-tests tasks
/agent fix-tests
/agent commit
```

И Codex будет делать всё автоматически.

---

# 1️⃣ Сначала создаём только базовый проект

В терминале:

```bash
mkdir codex-task-manager
cd codex-task-manager

git init

python -m venv venv
source venv/bin/activate
```

Установи зависимости:

```bash
pip install fastapi uvicorn pytest httpx
pip freeze > requirements.txt
```

Теперь **дальше всё будет делать Codex**.

---

# 2️⃣ Создай файл AGENTS.md

Этот файл — **инструкция для Codex агентов**.

`AGENTS.md`

```markdown
# Codex Agents Configuration

## ProjectAgent

Основной агент проекта.

Responsibilities:

- создавать структуру проекта
- генерировать модули
- генерировать API роуты
- создавать тесты
- исправлять ошибки
- обновлять архитектуру
- коммитить изменения в GitHub

Capabilities:

- generate_project_structure
- generate_router
- generate_controller
- generate_service
- generate_repository
- generate_tests
- fix_tests
- update_architecture
- git_commit
```

---

# 3️⃣ Создай SKILLS.md

`SKILLS.md`

```markdown
# Codex Skills

## generate_project_structure

Создает структуру проекта Python FastAPI.

Structure:

src/
modules/
controllers/
routers/
middleware/
interfaces/
utils/

tests/
unit/
integration/


## generate_router

Создает FastAPI router для модуля.

## generate_controller

Создает controller слой.

## generate_service

Создает business logic слой.

## generate_repository

Создает data access слой.

## pagination

Добавляет поддержку пагинации.

## filtering

Добавляет фильтрацию задач.

## generate_tests

Создает unit и integration тесты.

## fix_tests

Исправляет failing тесты.

## git_commit

Коммитит изменения в GitHub.
```

---

# 4️⃣ Создай CONTROL_FLOW.md

`CONTROL_FLOW.md`

```markdown
# Codex Control Flow

create-project

1 generate_project_structure
2 generate_router
3 generate_controller
4 generate_service
5 generate_repository
6 generate_tests
7 commit

fix-bugs

1 run_tests
2 detect_failures
3 fix_tests
4 rerun_tests
5 commit

update-architecture

1 analyze_project
2 update_architecture
3 update_modules
4 commit
```

---

# 5️⃣ ARCHITECTURE.md

Этот файл Codex использует для генерации кода.

`architecture.md`

```markdown
# Architecture

Используется Layered Architecture.

Layers:

Router
Controller
Service
Repository
Data

Каждый модуль должен иметь:

router
controller
service
repository
tests

Modules:

tasks
users (future)
auth (future)
```

---

# 6️⃣ TESTING.md

`testing.md`

```markdown
# Testing Strategy

Testing framework:

pytest

Types of tests:

Unit tests
tests/unit

Integration tests
tests/integration

Requirements:

каждый сервис должен иметь unit тест
каждый router должен иметь integration тест
coverage >= 80%
```

---

# 7️⃣ Команды которые ты будешь писать Codex

Теперь в **VS Code Codex Agent** ты пишешь команды.

---

## Создать проект

В Codex:

```
Create project structure using architecture.md
```

или

```
/agent create-project
```

Codex автоматически создаст:

```
src/
modules/
controllers/
routers/
middleware/
interfaces/
utils/

tests/
unit/
integration/
```

---

# 8️⃣ Сгенерировать модуль задач

Команда:

```
Generate module tasks according to architecture.md
```

Codex создаст:

```
src/modules/tasks
src/controllers/task_controller.py
src/routers/task_router.py
tests/unit/test_task_service.py
tests/integration/test_task_api.py
```

---

# 9️⃣ Сгенерировать роуты

Команда:

```
Generate CRUD router for tasks
```

Codex сам создаст:

```
GET /tasks
POST /tasks
PATCH /tasks/{id}
DELETE /tasks/{id}
```

---

# 🔟 Сгенерировать тесты

Команда:

```
Generate tests for tasks module according to testing.md
```

Codex создаст:

```
unit tests
integration tests
```

---

# 11️⃣ Исправить баги

Команда:

```
Run tests and fix failing tests
```

Codex:

1 запускает pytest
2 анализирует ошибки
3 исправляет код
4 снова запускает тесты

---

# 12️⃣ Обновить архитектуру

Команда:

```
Analyze project and update architecture if needed
```

Codex:

* рефакторит код
* обновляет architecture.md
* переносит файлы

---

# 13️⃣ Коммит в GitHub

Команда:

```
Commit changes to GitHub with descriptive message
```

Codex выполнит:

```
git add .
git commit -m "update tasks module"
git push
```

---

# 14️⃣ GitHub Actions

Создай один файл:

`.github/workflows/tests.yml`

И скажи Codex:

```
Create GitHub CI workflow for pytest
```

Он сам создаст pipeline.

---

# 💡 Как будет выглядеть твоя работа

В IDE ты пишешь:

```
Create FastAPI task manager project using architecture.md
```

Codex:

* создаёт структуру
* создаёт модули
* создаёт тесты
* создаёт API
* запускает тесты

---

Потом:

```
Add filtering and pagination to tasks
```

Codex обновляет:

```
router
service
tests
```

---

Потом:

```
Run tests and fix errors
```

---

# 🔥 Если хочешь, я покажу **самую мощную конфигурацию Codex IDE**, которую используют senior devs:

там появляется **4 автономных агента**:

* Architect Agent
* Backend Agent
* Testing Agent
* Refactor Agent

И проект **сам себя улучшает после каждого коммита**.
