# Development

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
cp .env.example .env
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
```

## Run app

```bash
PYTHONPATH=src python -m flask --app wsgi:app run --debug
```

## Run checks

```bash
python -m ruff check .
python -m black --check .
python -m pytest
```

## Creating a migration

```bash
PYTHONPATH=src python -m flask --app wsgi:app db migrate -m "describe change"
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
```
