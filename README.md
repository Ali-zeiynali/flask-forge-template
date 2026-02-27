<p align="center">
  <img src="assets/images/logo.png" width="380" alt="Flask Forge Template Logo"/>
</p>

<h1 align="center">Flask Forge Template 🚀</h1>

<p align="center">
Production-ready Flask API template with secure authentication, RBAC, modern tooling, and clean architecture.
</p>

<p align="center">
  Built for real-world backend systems — not just demos.
</p>

---

# 🔥 Why Flask Forge Template?

Starting a Flask project usually means:

- Rewriting auth from scratch  
- Reinventing RBAC  
- Wiring CI, linting, formatting  
- Setting up Docker  
- Fighting with migrations  
- Adding security headers later  
- Writing tests “someday”  

**Flask Forge Template solves all of that upfront.**

It gives you a structured, scalable, security-aware backend foundation — ready for production workflows.

---

# ✨ Core Features

### 🔐 Authentication
- JWT-based authentication
- Register / Login / Refresh / Logout / Me
- Secure password hashing (bcrypt/argon2)
- Token protection & validation

### 🛡️ Authorization (RBAC)
- Role-Based Access Control
- Permission system (`users:read`, `users:write`, etc.)
- Decorators:
  - `@require_auth`
  - `@require_roles`
  - `@require_permissions`
  - Owner-or-permission checks

### 🧱 Clean Architecture
- Feature-based API modules
- Centralized error handling
- Standardized response envelope
- Config-driven environment setup

### 🧪 Testing & Quality
- pytest test suite
- Coverage support
- Fixture-based isolation
- CI enforced quality gates

### 🔎 Code Quality
- ruff (linting)
- black (formatting)
- Strict style enforcement
- Optional security scan via bandit

### 🔒 Security
- Security headers (CSP, HSTS, etc.)
- Password hashing best practices
- Optional rate limiting
- Dependency audit support (`pip-audit`)

### 🗄️ Database
- SQLAlchemy 2.x
- Flask-Migrate / Alembic
- Migration-first workflow

### 🐳 Docker
- Dockerfile ready
- docker-compose for development

### 🌐 Built-in Landing Page
- Tailwind-powered dark theme
- Health & system overview
- Next steps guidance
- Confirms correct setup

---

# 🚀 Quickstart

## Windows (PowerShell)

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
````

Open:

```
http://127.0.0.1:5000
```

---

## macOS / Linux (bash)

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

---

# 🛠 Development Commands

```bash
# Lint
python -m ruff check .

# Format check
python -m black --check .

# Run tests
PYTHONPATH=src python -m pytest

# Run tests with coverage
PYTHONPATH=src python -m pytest --cov=src --cov-report=term-missing

# Security scan
python -m bandit -r src
python -m pip_audit
```

---

# 🏗 Project Structure

```
src/
  api/            # API modules (health, auth, users, admin)
  core/           # errors, responses, authz, security helpers
  extensions/     # db, migrate, jwt, cors, security headers
  web/            # landing blueprint + templates
  cli.py          # custom forge CLI commands
  app.py          # application factory
  wsgi.py         # entrypoint

tests/            # pytest test suite
docs/             # in-depth documentation
assets/           # project assets (logo, images)
```

---

# 🔐 RBAC Example

Protect an endpoint:

```python
@require_permissions("users:read")
def get_users():
    ...
```

Admin-only route:

```python
@require_roles("admin")
def create_role():
    ...
```

---

# 📚 Documentation

* [API Overview](docs/api.md)
* [Authentication Guide](docs/auth.md)
* [RBAC Guide](docs/rbac.md)
* [Security Guide](docs/security.md)
* [CLI Commands](docs/cli.md)
* [Testing Guide](docs/testing.md)

---

# 🧪 Testing Philosophy

This template enforces:

* Isolated test DB
* Real auth flows in tests
* Permission boundary validation
* Negative case testing (401 / 403 / 404 / 409)

Production-ready behavior is tested — not just happy paths.

---

# 🤝 Contributing

We welcome improvements.

Workflow:

1. Create issue
2. Create feature branch
3. Run lint & tests
4. Open PR to `develop`
5. CI must pass

See: [CONTRIBUTING.md](CONTRIBUTING.md)

---

# 🔒 Security

If you discover a vulnerability:

* Do NOT open a public issue
* Follow instructions in [SECURITY.md](SECURITY.md)

Security documentation:

* [docs/security.md](docs/security.md)

---

# 🗺 Roadmap

Future improvements:

* OpenAPI / Swagger UI
* Async support option
* Plugin system
* Form builder utilities
* Audit logging
* Multi-tenant support
* Redis-backed rate limiting
* Observability (structured logging / tracing)

---

# 📄 License

MIT License
See [LICENSE](LICENSE)

---

# ⭐ Final Notes

Flask Forge Template is designed to be:

* Structured
* Secure
* Scalable
* Developer-friendly
* Production-minded

If you find it useful, ⭐ the repo and contribute.