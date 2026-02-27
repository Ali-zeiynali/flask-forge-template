from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import create_app
from cli import seed_rbac
from core.security import hash_password
from extensions.db import db
from models import Role, User


@pytest.fixture()
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        seed_rbac()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def users(app):
    admin_role = Role.query.filter_by(name="admin").first()
    user_role = Role.query.filter_by(name="user").first()
    admin = User(
        email="admin@example.com",
        full_name="Admin",
        password_hash=hash_password("Password123"),
        is_active=True,
    )
    regular = User(
        email="user@example.com",
        full_name="User",
        password_hash=hash_password("Password123"),
        is_active=True,
    )
    admin.roles.append(admin_role)
    regular.roles.append(user_role)
    db.session.add_all([admin, regular])
    db.session.commit()
    return {"admin": admin, "user": regular}


def _auth_headers(client, email: str, password: str) -> dict[str, str]:
    response = client.post("/api/auth/login", json={"email": email, "password": password})
    token = response.get_json()["data"]["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture()
def admin_headers(client, users):
    _ = users
    return _auth_headers(client, "admin@example.com", "Password123")


@pytest.fixture()
def user_headers(client, users):
    _ = users
    return _auth_headers(client, "user@example.com", "Password123")
