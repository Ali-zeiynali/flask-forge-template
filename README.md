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
