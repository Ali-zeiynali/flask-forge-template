# Flask Forge Template

A minimal, production-oriented Flask API template for fast project bootstrapping.

## Features

- Flask app factory and WSGI entrypoint
- Health endpoint at `/api/health`
- SQLAlchemy + Flask-Migrate wiring
- Environment-based configuration
- Structured logging setup
- Pytest test suite
- Ruff + Black code quality tooling
- GitHub Actions CI
- Docker and docker-compose support

## Prerequisites

- Python 3.12+
- pip
- virtualenv (recommended)

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
PYTHONPATH=src flask --app wsgi:app run --debug
```

API will be available at `http://127.0.0.1:5000`.

## Development Commands

```bash
make run
make test
make lint
make format
```

## Environment Variables

See `.env.example`.

- `FLASK_ENV`: `development` | `testing` | `production`
- `SECRET_KEY`: Flask secret key
- `APP_NAME`: Application name
- `DATABASE_URL`: SQLAlchemy database URL
- `LOG_LEVEL`: Logging level (`DEBUG`, `INFO`, ...)

## Project Structure

```text
.
├── src/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── extensions/
│   ├── utils/
│   ├── app.py
│   ├── config.py
│   └── wsgi.py
├── tests/
├── docs/
├── scripts/
└── .github/workflows/
```

## License

MIT
