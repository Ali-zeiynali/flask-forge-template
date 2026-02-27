# Flask Forge Template

Production-minded Flask API template with JWT auth, RBAC, migrations, tests, CI, and Docker.

## Quickstart (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
$env:PYTHONPATH="src"
python -m flask --app wsgi:app db upgrade
python -m flask --app wsgi:app forge seed
python -m flask --app wsgi:app forge create-admin --email admin@example.com --password Password123
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
PYTHONPATH=src python -m flask --app wsgi:app forge seed
PYTHONPATH=src python -m flask --app wsgi:app forge create-admin --email admin@example.com --password Password123
PYTHONPATH=src python -m flask --app wsgi:app run --debug
```

## Core APIs

- Health: `GET /api/health` (legacy + `/api/v1/health`)
- Auth: `/api/auth/register|login|refresh|logout|me`
- Users: `/api/users` CRUD (legacy + `/api/v1/users`)
- Admin (admin role only): `/api/admin/roles`, `/api/admin/permissions`, `/api/admin/users/{id}/roles`

## Quality checks

```bash
python -m ruff check .
python -m black --check .
python -m pytest
```

## Migrations

```bash
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
PYTHONPATH=src python -m flask --app wsgi:app db migrate -m "message"
```

## Auth and permission model

Default roles: `admin`, `staff`, `user`.

Default permissions: `users:read`, `users:write`, `roles:read`, `roles:write`.

Users endpoints are protected by decorators:

- `@require_auth`
- `@require_roles(*roles)`
- `@require_permissions(*permissions)`
- `@require_owner_or_permission(permission, owner_param="user_id")`

## Example curl

```bash
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"Password123"}'

curl http://127.0.0.1:5000/api/auth/me \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```
