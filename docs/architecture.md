# Architecture

## Runtime layout

- `src/app.py`: application factory and extension/blueprint registration.
- `src/wsgi.py`: WSGI entrypoint.
- `src/config.py`: environment-aware config classes.
- `src/api/`: API modules (`health`, `users`).
- `src/core/`: shared concerns (logging, errors, response schema).
- `src/extensions/`: integration points for db/migrations/cors/jwt placeholder.

## Request flow

1. `create_app` loads selected config.
2. Extensions are initialized (`db`, `migrate`, `cors`, `jwt placeholder`).
3. Blueprints are mounted under `/api`.
4. Errors are normalized by `core.errors.register_error_handlers`.

## Data layer

- SQLAlchemy model `User` lives in `src/api/users.py`.
- SQLite is default for local dev.
- Migrations are managed through Flask-Migrate + Alembic.
