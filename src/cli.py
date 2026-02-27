from __future__ import annotations

import click
from flask import Flask
from flask_migrate import current as migration_current

from core.security import hash_password
from core.settings import safe_config_snapshot
from extensions.db import db
from models import Permission, Role, User

DEFAULT_ROLE_PERMISSIONS = {
    "admin": [
        "users:read",
        "users:write",
        "roles:read",
        "roles:write",
        "permissions:read",
        "permissions:write",
    ],
    "staff": ["users:read", "users:write", "roles:read", "permissions:read"],
    "user": [],
}


def seed_rbac() -> None:
    permissions_map: dict[str, Permission] = {}
    for permissions in DEFAULT_ROLE_PERMISSIONS.values():
        for perm_name in permissions:
            permission = Permission.query.filter_by(name=perm_name).first()
            if permission is None:
                permission = Permission(name=perm_name)
                db.session.add(permission)
            permissions_map[perm_name] = permission

    db.session.flush()

    for role_name, perm_names in DEFAULT_ROLE_PERMISSIONS.items():
        role = Role.query.filter_by(name=role_name).first()
        if role is None:
            role = Role(name=role_name)
            db.session.add(role)
        role.permissions = [permissions_map[name] for name in perm_names]

    db.session.commit()


def register_cli_commands(app: Flask) -> None:
    @app.cli.group("forge")
    def forge_cli():
        """FlaskForge project management commands."""

    @forge_cli.command("seed")
    def forge_seed():
        seed_rbac()
        click.echo("Seeded roles and permissions.")

    @forge_cli.command("create-admin")
    @click.option("--email", required=True)
    @click.option("--password", required=True)
    @click.option("--full-name", default="Administrator")
    def forge_create_admin(email: str, password: str, full_name: str):
        seed_rbac()
        user = User.query.filter_by(email=email.lower()).first()
        if user is None:
            user = User(
                email=email.lower(),
                full_name=full_name,
                password_hash=hash_password(password),
                is_active=True,
            )
            db.session.add(user)
        else:
            user.full_name = full_name
            user.password_hash = hash_password(password)
            user.is_active = True

        admin_role = Role.query.filter_by(name="admin").first()
        if admin_role and admin_role not in user.roles:
            user.roles.append(admin_role)

        db.session.commit()
        click.echo(f"Admin user ready: {email.lower()}")

    @forge_cli.command("doctor")
    def forge_doctor():
        healthy_db = True
        try:
            db.session.execute(db.text("SELECT 1"))
        except Exception:
            healthy_db = False

        click.echo("FlaskForge doctor report")
        click.echo(f"- db_connection: {'ok' if healthy_db else 'failed'}")
        click.echo(f"- migrations_revision: {migration_current()}")
        for key, value in safe_config_snapshot(dict(app.config)).items():
            click.echo(f"- {key}: {value}")
