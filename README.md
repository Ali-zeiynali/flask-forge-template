<p align="center">
  <img src="assets/images/logo.png" width="380" alt="Flask Forge Template Logo"/>
</p>

<h1 align="center">Flask Forge Template 🚀</h1>

<p align="center">
  <b>Production-ready Flask API starter</b> with <b>JWT Auth</b>, <b>RBAC</b>, <b>migrations</b>, <b>tests</b>, <b>Docker</b>, and a clean <b>service/repo</b> architecture — built for real teams, not toy demos.
</p>

<p align="center">
  <a href="https://github.com/Ali-zeiynali/flask-forge-template">GitHub Repo</a> •
  <a href="docs/index.md">Docs</a> •
  <a href="LICENSE">License</a>
</p>

---

## ✨ Overview

**Flask Forge Template** is a modern **Flask backend template** maintained by **Ali Zeiynali** to bootstrap real-world services faster.

Instead of spending your first week rebuilding **authentication**, **RBAC**, **migrations**, **testing**, **Docker**, and API structure, you can clone this template and start shipping product logic from day one.

- 🔗 Repository: https://github.com/Ali-zeiynali/flask-forge-template
- 👤 Maintainer: Ali Zeiynali
- 📩 Contact: Azeiynali@gmail.com

---

## ✅ What’s Included (Implemented)

This template ships with an opinionated, production-minded baseline:

### 🔐 Authentication (JWT)

- Register / Login / Refresh / Logout / Me
- Secure password hashing
- Standard JWT error handling (expired/invalid/missing token)

### 🛡️ Authorization (RBAC + Permissions)

- Roles + permissions stored in the database
- Decorators for:
    - role checks
    - permission checks
    - owner-or-permission checks
- Admin endpoints for managing roles/permissions and assignments

### 🧱 Architecture (Clean API Design)

- App factory pattern + config classes (`development`, `testing`, `production`)
- Route → Schema → Service → Repo separation (feature-based)
- Unified error/response contract (consistent JSON envelope)

### 🗄️ Database & Migrations

- SQLAlchemy + Flask-Migrate/Alembic
- Seed commands for default RBAC setup

### 🧪 Testing & Quality

- Pytest suite: auth, users, admin, health, web
- Lint/format/audit scripts
- GitHub Actions CI (ruff + black + pytest)

### 🐳 Docker

- Dockerfile + docker-compose for containerized runs

### 🌙 Built-in Landing Page

- A dark, modern `/` landing page to confirm setup and show “next steps”
- Health endpoints at `/api/health` and `/api/v1/health`

---

## 🗂 Project Layout

```text
src/
  flaskforge/
    app.py                # Flask app factory
    wsgi.py               # Canonical CLI/Gunicorn entrypoint
    cli.py                # Custom `flask forge ...` commands
    config.py             # Config + env var mapping

    core/                 # authz, errors, security, response helpers
    extensions/           # db, jwt, migrate, cors, security headers
    api/v1/               # versioned API modules (health/auth/users/admin)
    web/                  # landing page blueprint + templates
    migrations/           # Alembic migrations

docs/                     # Documentation (how to use & extend the template)
scripts/                  # Bootstrap / lint / test / format / audit helpers
tests/                    # Pytest test suite
assets/                   # Logos and images
```

---

## 🚀 Quickstart (Local Development)

### Requirements

- 🐍 Python **3.12+**
- 🔧 Git

### macOS / Linux (bash)

```bash
bash scripts/bootstrap.sh
```

Then run:

```bash
source .venv/bin/activate
PYTHONPATH=src python -m flask --app flaskforge.wsgi:app run --debug
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap.ps1
```

Then run:

```powershell
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH="src"
python -m flask --app flaskforge.wsgi:app run --debug
```

---

## 🔎 Verify It’s Working

- 🌙 Landing page: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- ❤️ Health: [http://127.0.0.1:5000/api/health](http://127.0.0.1:5000/api/health)
- ❤️ v1 Health: [http://127.0.0.1:5000/api/v1/health](http://127.0.0.1:5000/api/v1/health)

---

## 🐳 Run With Docker

### Docker

```bash
docker build -t flask-forge-template .
docker run --rm -p 8000:8000 --env-file .env flask-forge-template
```

Open:

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

### docker-compose

```bash
docker compose up --build
```

---

## ⚙️ Configuration

All configuration is env-driven in `flaskforge/config.py`.

1. Copy `.env.example` → `.env`
2. Set:

- `APP_ENV` (`development` / `testing` / `production`)
- `DATABASE_URL`
- `SECRET_KEY`, `JWT_SECRET_KEY`
- `CORS_ORIGINS`
- Security toggles (headers/HSTS/HTTPS) if enabled

See: **[docs/configuration.md](docs/configuration.md)**

---

## 🧰 Daily Dev Commands

```bash
# Lint / Format / Tests / Audit
bash scripts/lint.sh
bash scripts/format.sh
bash scripts/test.sh
bash scripts/audit.sh

# Migrations + seed
bash scripts/init_db.sh
```

---

## 👑 DB + Seed + Create Admin

```bash
PYTHONPATH=src python -m flask --app flaskforge.wsgi:app db upgrade
PYTHONPATH=src python -m flask --app flaskforge.wsgi:app forge seed
PYTHONPATH=src python -m flask --app flaskforge.wsgi:app forge create-admin \
  --email admin@yourdomain.com \
  --password '<strong-password>' \
  --full-name 'Admin User'
```

---

## 🧭 Next Steps (Using This as Your Own Project)

1. Update branding + metadata (project name/version/docs title).
2. Change secrets and DB settings in `.env`.
3. Adjust RBAC defaults in CLI seed config.
4. Add new API modules under `api/v1/<feature>/` using route → schema → service → repo.
5. Update landing page links (Docs/GitHub) if you host docs on GitHub Pages.
6. Add deployment targets (gunicorn, Docker, CI/CD, cloud).

---

## 📚 Documentation Map

- 📌 [Docs Index](docs/index.md)
- 🧱 [Architecture](docs/architecture.md)
- ⚙️ [Configuration](docs/configuration.md)
- 🧑‍💻 [Development](docs/development.md)
- 🔌 [API Reference](docs/api.md)
- 🔐 [Auth Guide](docs/auth.md)
- 🛡️ [RBAC Guide](docs/rbac.md)
- 🧰 [CLI Guide](docs/cli.md)
- 🧪 [Testing](docs/testing.md)
- 🚢 [Deployment](docs/deployment.md)
- 🔒 [Security](docs/security.md)

---

## 🤝 Contributing

PRs are welcome. Please read:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

---

## 🔒 Security

If you discover a vulnerability, please follow:

- [SECURITY.md](SECURITY.md)

---

## 📄 License

MIT — see [LICENSE](LICENSE).
