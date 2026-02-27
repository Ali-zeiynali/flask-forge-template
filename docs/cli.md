# CLI Commands

The project exposes custom commands under `flask forge`.

## Entry point

```bash
python -m flask --app flaskforge.wsgi:app <command>
```

## Commands

### Migrations

```bash
python -m flask --app flaskforge.wsgi:app db upgrade
python -m flask --app flaskforge.wsgi:app db migrate -m "message"
```

### RBAC seed

```bash
python -m flask --app flaskforge.wsgi:app forge seed
```

### Create/update admin

```bash
python -m flask --app flaskforge.wsgi:app forge create-admin --email admin@yourdomain.com --password '<strong-password>' --full-name 'Admin User'
```

### Environment diagnostics

```bash
python -m flask --app flaskforge.wsgi:app forge doctor
```
