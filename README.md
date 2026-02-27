# Flask Forge Template

Production-minded Flask API template with app factory, SQLAlchemy, migrations, test suite, and CI.

## What you get

- App factory (`src/app.py`) + WSGI entrypoint (`src/wsgi.py`)
- Health endpoint: `GET /api/health` -> `{"status":"ok"}`
- Real CRUD example: `users` module (`POST/GET/LIST/PATCH/DELETE`)
- Flask-SQLAlchemy + Flask-Migrate (SQLite by default)
- Unified API success/error response format
- Ruff + Black + Pytest + GitHub Actions CI
- Docker and docker-compose for local development

## Requirements

- Python 3.12+
- pip

## Quickstart (PowerShell / Windows)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
$env:PYTHONPATH="src"
python -m flask --app wsgi:app db upgrade
python -m flask --app wsgi:app run --debug
```

## Quickstart (bash)

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
cp .env.example .env
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
PYTHONPATH=src python -m flask --app wsgi:app run --debug
```

## Quality checks

```bash
python -m ruff check .
python -m black --check .
python -m pytest
```

## API overview

- `GET /api/health`
- `POST /api/users`
- `GET /api/users/{id}`
- `GET /api/users?page=1&per_page=10`
- `PATCH /api/users/{id}`
- `DELETE /api/users/{id}`

See `docs/api.md` for full request/response examples.

## Database migrations

```bash
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
PYTHONPATH=src python -m flask --app wsgi:app db migrate -m "message"
```

Alembic configuration is in `alembic.ini`, and migration scripts are under `src/migrations/versions`.

## Project structure

```text
src/
  api/
    health.py
    users.py
  core/
  extensions/
  app.py
  config.py
  wsgi.py
tests/
docs/
```

## Documentation

- `docs/index.md`
- `docs/architecture.md`
- `docs/configuration.md`
- `docs/development.md`
- `docs/api.md`
- `docs/deployment.md`

## License

MIT
