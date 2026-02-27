# Architecture

## Runtime layout

- `src/app.py`: application factory and extension/blueprint registration.
- `src/flaskforge/wsgi.py`: package-based WSGI entrypoint for Flask CLI.
- `src/config.py`: environment-aware config classes.
- `src/api/v1/`: versioned API modules (`health`, `auth`, `users`, `admin`).
- `src/core/`: shared concerns (logging, errors, response contract, authz).
- `src/extensions/`: db/migrations/cors/jwt/security-headers integrations.

Compatibility aliases are kept in `src/api/*.py` so both `/api/*` and `/api/v1/*` stay active.

## Request flow

1. `create_app` loads selected config and initializes extensions.
2. JWT, DB, migrations, CORS, and security headers are wired from config.
3. Blueprints are mounted for both `/api` and `/api/v1`.
4. Errors are normalized by `core.errors.register_error_handlers`.

## Data layer

- Core models live in `src/models.py`: `User`, `Role`, `Permission`, and association tables.
- SQLite is default for local development.
- Migrations are managed through Flask-Migrate + Alembic in `src/migrations`.
