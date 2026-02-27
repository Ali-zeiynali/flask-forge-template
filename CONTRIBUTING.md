# Contributing

Thanks for investing time in this project.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
cp .env.example .env
```

PowerShell notes:

```powershell
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH="src"
```

## Run locally

```bash
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
PYTHONPATH=src python -m flask --app wsgi:app run --debug
```

## Quality gates

```bash
python -m ruff check .
python -m black --check .
python -m pytest
```

## Pull requests

- Keep changes focused.
- Add/adjust tests for behavior changes.
- Update docs when behavior or setup changes.
- Update `CHANGELOG.md` for user-visible changes.
