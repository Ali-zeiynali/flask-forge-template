# CLI Commands

Use `python -m` style commands.

## Seed RBAC

```bash
PYTHONPATH=src python -m flask --app wsgi:app forge seed
```

## Create or update admin

```bash
PYTHONPATH=src python -m flask --app wsgi:app forge create-admin --email admin@example.com --password Password123
```

## Migrations

```bash
PYTHONPATH=src python -m flask --app wsgi:app db upgrade
PYTHONPATH=src python -m flask --app wsgi:app db migrate -m "message"
```
