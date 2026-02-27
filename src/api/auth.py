from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from flask import Blueprint, current_app, g, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)

from core.authz import require_auth
from core.errors import APIError, RateLimitError
from core.responses import created_response, success_response
from core.security import hash_password, verify_password
from extensions.db import db
from extensions.jwt import TOKEN_BLOCKLIST
from models import Role, User

auth_bp = Blueprint("auth", __name__)
_LOGIN_ATTEMPTS: dict[str, list[float]] = {}


def _validate_email_password(payload: dict[str, Any] | None) -> tuple[str, str]:
    if not payload:
        raise APIError("invalid_payload", "Request body is required.", 400)
    email = str(payload.get("email", "")).strip().lower()
    password = str(payload.get("password", ""))
    if not email or "@" not in email:
        raise APIError("invalid_email", "A valid email is required.", 400)
    if not password:
        raise APIError("invalid_password", "password is required.", 400)
    return email, password


def _check_login_rate_limit() -> None:
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


@auth_bp.post("/auth/register")
def register():
    payload = request.get_json(silent=True)
    email, password = _validate_email_password(payload)
    full_name = str((payload or {}).get("full_name", "")).strip()
    if not full_name:
        raise APIError("invalid_full_name", "full_name is required.", 400)
    if len(password) < 8:
        raise APIError("invalid_password", "password must be at least 8 characters.", 400)

    if User.query.filter_by(email=email).first() is not None:
        raise APIError("email_conflict", "User with this email already exists.", 409)

    user = User(
        email=email, full_name=full_name, password_hash=hash_password(password), is_active=True
    )
    default_role = Role.query.filter_by(name="user").first()
    if default_role:
        user.roles.append(default_role)
    db.session.add(user)
    db.session.commit()
    return created_response(user.to_dict())


@auth_bp.post("/auth/login")
def login():
    _check_login_rate_limit()
    email, password = _validate_email_password(request.get_json(silent=True))
    user = User.query.filter_by(email=email).first()
    if user is None or not verify_password(user.password_hash, password):
        raise APIError("auth_invalid_credentials", "Invalid credentials.", 401)
    if not user.is_active:
        raise APIError("auth_inactive", "Inactive user.", 403)

    access_token = create_access_token(
        identity=str(user.id), additional_claims={"roles": [r.name for r in user.roles]}
    )
    refresh_token = create_refresh_token(identity=str(user.id))
    return success_response({"access_token": access_token, "refresh_token": refresh_token})


@auth_bp.post("/auth/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    user = db.session.get(User, int(identity))
    if user is None:
        raise APIError("auth_invalid_user", "Authentication required.", 401)
    access_token = create_access_token(
        identity=identity, additional_claims={"roles": [r.name for r in user.roles]}
    )
    return success_response({"access_token": access_token})


@auth_bp.post("/auth/logout")
@jwt_required()
def logout():
    token = get_jwt()
    exp = token.get("exp")
    if exp:
        TOKEN_BLOCKLIST[token["jti"]] = float(exp)
    return success_response({"message": "Logged out."})


@auth_bp.get("/auth/me")
@require_auth
def me():
    return success_response(g.current_user.to_dict())
