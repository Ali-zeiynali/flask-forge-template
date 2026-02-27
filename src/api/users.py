from __future__ import annotations

from typing import Any

from flask import Blueprint, request

from core.authz import require_owner_or_permission, require_permissions
from core.errors import APIError
from core.responses import created_response, no_content_response, success_response
from extensions.db import db
from models import User

users_bp = Blueprint("users", __name__)


def _validate_create_payload(payload: dict[str, Any] | None) -> tuple[str, str, str, bool]:
    if not payload:
        raise APIError("invalid_payload", "Request body is required.", 400)

    email = str(payload.get("email", "")).strip().lower()
    full_name = str(payload.get("full_name", "")).strip()
    password = str(payload.get("password", "")).strip()
    is_active = payload.get("is_active", True)

    if not email or "@" not in email:
        raise APIError("invalid_email", "A valid email is required.", 400)
    if not full_name:
        raise APIError("invalid_full_name", "full_name is required.", 400)
    if not password or len(password) < 8:
        raise APIError("invalid_password", "password must be at least 8 characters.", 400)
    if not isinstance(is_active, bool):
        raise APIError("invalid_is_active", "is_active must be a boolean.", 400)

    return email, full_name, password, is_active


def _validate_patch_payload(payload: dict[str, Any] | None) -> dict[str, Any]:
    if not payload:
        raise APIError("invalid_payload", "Request body is required.", 400)

    allowed_keys = {"email", "full_name", "is_active"}
    invalid_keys = set(payload) - allowed_keys
    if invalid_keys:
        raise APIError("invalid_fields", "Unsupported fields were provided.", 400)

    updates: dict[str, Any] = {}

    if "email" in payload:
        email = str(payload["email"]).strip().lower()
        if not email or "@" not in email:
            raise APIError("invalid_email", "A valid email is required.", 400)
        updates["email"] = email

    if "full_name" in payload:
        full_name = str(payload["full_name"]).strip()
        if not full_name:
            raise APIError("invalid_full_name", "full_name cannot be empty.", 400)
        updates["full_name"] = full_name

    if "is_active" in payload:
        is_active = payload["is_active"]
        if not isinstance(is_active, bool):
            raise APIError("invalid_is_active", "is_active must be a boolean.", 400)
        updates["is_active"] = is_active

    if not updates:
        raise APIError("empty_update", "At least one valid field must be provided.", 400)

    return updates


def _get_user_or_404(user_id: int) -> User:
    user = db.session.get(User, user_id)
    if user is None:
        raise APIError("not_found", "User not found.", 404)
    return user


@users_bp.post("/users")
@require_permissions("users:write")
def create_user():
    from core.security import hash_password

    email, full_name, password, is_active = _validate_create_payload(request.get_json(silent=True))

    if User.query.filter_by(email=email).first() is not None:
        raise APIError("email_conflict", "User with this email already exists.", 409)

    user = User(
        email=email,
        full_name=full_name,
        password_hash=hash_password(password),
        is_active=is_active,
    )
    db.session.add(user)
    db.session.commit()

    return created_response(user.to_dict())


@users_bp.get("/users/<int:user_id>")
@require_owner_or_permission("users:read")
def get_user(user_id: int):
    user = _get_user_or_404(user_id)
    return success_response(user.to_dict())


@users_bp.get("/users")
@require_permissions("users:read")
def list_users():
    page = request.args.get("page", default=1, type=int)
    page_size = request.args.get(
        "page_size", request.args.get("per_page", default=10, type=int), type=int
    )

    if page < 1 or page_size < 1:
        raise APIError("invalid_pagination", "page and page_size must be positive integers.", 400)

    pagination = User.query.order_by(User.id.asc()).paginate(
        page=page,
        per_page=min(page_size, 100),
        error_out=False,
    )

    return success_response(
        [user.to_dict() for user in pagination.items],
        meta={
            "page": pagination.page,
            "page_size": pagination.per_page,
            "total": pagination.total,
            "has_next": pagination.has_next,
        },
    )


@users_bp.patch("/users/<int:user_id>")
@require_owner_or_permission("users:write")
def update_user(user_id: int):
    user = _get_user_or_404(user_id)
    updates = _validate_patch_payload(request.get_json(silent=True))

    if "email" in updates:
        existing = User.query.filter(User.email == updates["email"], User.id != user.id).first()
        if existing is not None:
            raise APIError("email_conflict", "User with this email already exists.", 409)

    for field_name, value in updates.items():
        setattr(user, field_name, value)

    db.session.commit()
    return success_response(user.to_dict())


@users_bp.delete("/users/<int:user_id>")
@require_permissions("users:write")
def delete_user(user_id: int):
    user = _get_user_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return no_content_response()
