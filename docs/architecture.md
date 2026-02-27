# Architecture

## Runtime structure

- `src/app.py`: app factory, extension setup, blueprint registration.
- `src/flaskforge/wsgi.py`: canonical package entrypoint.
- `src/wsgi.py`: compatibility entrypoint used by Docker command.
- `src/config.py`: config classes and env parsing.
- `src/models.py`: user/role/permission models and association tables.

## API module pattern

`src/api/v1/users` demonstrates the preferred pattern:

- `routes.py`: HTTP handlers and decorators
- `schemas.py`: request parsing/validation
- `service.py`: business logic
- `repo.py`: DB access helpers
- `models.py`: module-facing model aliases

Apply this same structure for new domain modules.

## Request lifecycle

1. `create_app` loads config class.
2. Extensions (`db`, `migrate`, `jwt`, `cors`, security headers) are initialized.
3. Web blueprint mounts `/`.
4. API blueprints mount on `/api` and `/api/v1`.
5. Errors are normalized by global error handlers.
