# Flask Forge Template 🚀

A production-ready Flask starter focused on clean APIs, secure authentication, role-based access control, and a modern developer workflow.

## Features

- 🔐 JWT Auth (register/login/refresh/logout/me)
- 🛡️ RBAC + Permissions + Decorators
- 🧱 Clean Architecture
- 🧪 Tests + Fixtures + Coverage
- ✅ CI (GitHub Actions)
- 🐳 Docker + Compose
- 🗄️ SQLAlchemy + Migrations
- 🌐 Landing Page (Tailwind Dark)
- 🔎 Lint/Format (ruff/black)
- 🔒 Security Headers + Audit tools

## Quickstart (Windows PowerShell)

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

## Commands

```bash
python -m ruff check .
python -m black --check .
PYTHONPATH=src python -m pytest
PYTHONPATH=src python -m pytest --cov=src --cov-report=term-missing
python -m bandit -r src
python -m pip_audit
PYTHONPATH=src python -m flask --app wsgi:app forge seed
```

## Project Structure

```text
src/
  api/            # API blueprints (health, auth, users, admin)
  core/           # authz, errors, responses, security
  extensions/     # db, migrate, jwt, cors, security headers
  web/            # landing blueprint and template
  app.py          # app factory
  cli.py          # forge commands
tests/            # pytest test suite
docs/             # detailed documentation
```

## API Reference

- [API Overview](docs/api.md)
- [Auth Guide](docs/auth.md)
- [RBAC Guide](docs/rbac.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md) and [docs/security.md](docs/security.md).

## License

MIT — see [LICENSE](LICENSE).
