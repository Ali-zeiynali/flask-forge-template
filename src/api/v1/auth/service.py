from __future__ import annotations

from datetime import UTC, datetime

from flask import current_app, g, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, get_jwt_identity

from core.errors import APIError, ConflictError, RateLimitError
from core.security import hash_password, verify_password
from extensions.db import db
from extensions.jwt import TOKEN_BLOCKLIST
from models import Role, User

_LOGIN_ATTEMPTS: dict[str, list[float]] = {}


def check_login_rate_limit() -> None:
    client_id = request.remote_addr or "unknown"
    if not current_app.config.get("RATE_LIMIT_ENABLED", True):
        return
    limit = current_app.config["RATE_LIMIT_LOGIN_PER_MINUTE"]
    now = datetime.now(UTC).timestamp()
    window_start = now - 60
    history = [value for value in _LOGIN_ATTEMPTS.get(client_id, []) if value >= window_start]
    if len(history) >= limit:
        raise RateLimitError("Too many login attempts.")
    history.append(now)
    _LOGIN_ATTEMPTS[client_id] = history


def register_user(email: str, full_name: str, password: str) -> dict[str, object]:
    if User.query.filter_by(email=email).first() is not None:
        raise ConflictError("User with this email already exists.")

    user = User(
        email=email,
        full_name=full_name,
        password_hash=hash_password(password),
        is_active=True,
    )
    default_role = Role.query.filter_by(name="user").first()
    if default_role:
        user.roles.append(default_role)

    db.session.add(user)
    db.session.commit()
    return user.to_dict()


def login_user(email: str, password: str) -> dict[str, str]:
    check_login_rate_limit()
    user = User.query.filter_by(email=email).first()
    if user is None or not verify_password(user.password_hash, password):
        raise APIError("auth_invalid_credentials", "Invalid credentials.", 401)
    if not user.is_active:
        raise APIError("auth_inactive", "Inactive user.", 403)

    return {
        "access_token": create_access_token(
            identity=str(user.id),
            additional_claims={"roles": [role.name for role in user.roles]},
        ),
        "refresh_token": create_refresh_token(identity=str(user.id)),
    }


def refresh_access_token() -> dict[str, str]:
    identity = get_jwt_identity()
    user = db.session.get(User, int(identity))
    if user is None:
        raise APIError("auth_invalid_user", "Authentication required.", 401)
    return {
        "access_token": create_access_token(
            identity=identity,
            additional_claims={"roles": [role.name for role in user.roles]},
        )
    }


def revoke_current_token() -> dict[str, str]:
    token = get_jwt()
    exp = token.get("exp")
    if exp:
        TOKEN_BLOCKLIST[token["jti"]] = float(exp)
    return {"message": "Logged out."}


def me() -> dict[str, object]:
    return g.current_user.to_dict()
