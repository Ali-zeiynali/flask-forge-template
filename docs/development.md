# Development

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
cp .env.example .env
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
PYTHONPATH=src python -m flask --app wsgi:app forge seed
```

## Create admin

```bash
PYTHONPATH=src python -m flask --app wsgi:app forge create-admin --email admin@example.com --password Password123
```

## Run

```bash
PYTHONPATH=src python -m flask --app wsgi:app run --debug
```

## Checks

```bash
python -m ruff check .
python -m black --check .
python -m pytest
```
