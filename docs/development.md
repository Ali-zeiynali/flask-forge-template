# Development Guide

## Prerequisites

- Python 3.12+
- Git

## Local bootstrap

### macOS / Linux

```bash
bash scripts/bootstrap.sh
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap.ps1
```

Both scripts install dependencies, create `.env` when needed, run migrations, and seed RBAC data.

## Run the app

### macOS / Linux

```bash
source .venv/bin/activate
python -m flask --app flaskforge.wsgi:app run --debug
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
python -m flask --app flaskforge.wsgi:app run --debug
```

## Verify startup

- Landing page: `http://127.0.0.1:5000/`
- Health endpoint: `http://127.0.0.1:5000/api/health`
- Versioned health endpoint: `http://127.0.0.1:5000/api/v1/health`

## Common workflows

```bash
# apply migrations
python -m flask --app flaskforge.wsgi:app db upgrade

# create new migration
python -m flask --app flaskforge.wsgi:app db migrate -m "describe change"

# seed RBAC
python -m flask --app flaskforge.wsgi:app forge seed

# create/update admin user
python -m flask --app flaskforge.wsgi:app forge create-admin --email admin@yourdomain.com --password '<strong-password>' --full-name 'Admin User'
```
