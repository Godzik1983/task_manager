# Architecture

Проект использует модульную Layered Architecture.

## Layers

Внутри каждого модуля применяются слои:

1. `router` - HTTP-эндпоинты FastAPI, преобразование доменных ошибок в HTTP-ответы.
2. `controller` - orchestration-слой между transport и бизнес-логикой.
3. `service` - бизнес-правила и валидация.
4. `repository` - доступ к данным (сейчас in-memory, далее можно заменить на БД).
5. `data` - Pydantic-модели запросов/ответов и внутренних сущностей.

Зависимости направлены строго сверху вниз:
`router -> controller -> service -> repository -> data`.

## Module Contract

Каждый модуль обязан содержать:

- `router.py`
- `controller.py`
- `service.py`
- `repository.py`
- `data.py`
- `tests/` (локальные модульные заглушки/тесты)

## Current Modules

- `tasks` - реализован (CRUD + unit/integration тесты в корневом `tests/`).
- `users` - future (скелет модуля создан).
- `auth` - future (скелет модуля создан).

## Testing Architecture

Глобальные тесты расположены по типам:

- `tests/unit` - unit-тесты сервисов.
- `tests/integration` - integration-тесты роутеров.

Для каждого нового модуля обязательно:

1. unit-тест для `service`;
2. integration-тест для `router`.
