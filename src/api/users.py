from __future__ import annotations

from typing import Any

from flask import Blueprint, request

from core.errors import APIError
from core.responses import created_response, no_content_response, success_response
from extensions.db import db

users_bp = Blueprint("users", __name__)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    full_name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
        }


def _validate_create_payload(payload: dict[str, Any] | None) -> tuple[str, str, bool]:
    if not payload:
        raise APIError("invalid_payload", "Request body is required.", 400)

    email = str(payload.get("email", "")).strip().lower()
    full_name = str(payload.get("full_name", "")).strip()
    is_active = payload.get("is_active", True)

    if not email or "@" not in email:
        raise APIError("invalid_email", "A valid email is required.", 400)
    if not full_name:
        raise APIError("invalid_full_name", "full_name is required.", 400)
    if not isinstance(is_active, bool):
        raise APIError("invalid_is_active", "is_active must be a boolean.", 400)

    return email, full_name, is_active


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
def create_user():
    email, full_name, is_active = _validate_create_payload(request.get_json(silent=True))

    if User.query.filter_by(email=email).first() is not None:
        raise APIError("email_conflict", "User with this email already exists.", 409)

    user = User(email=email, full_name=full_name, is_active=is_active)
    db.session.add(user)
    db.session.commit()

    return created_response(user.to_dict())


@users_bp.get("/users/<int:user_id>")
def get_user(user_id: int):
    user = _get_user_or_404(user_id)
    return success_response(user.to_dict())


@users_bp.get("/users")
def list_users():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    if page < 1 or per_page < 1:
        raise APIError("invalid_pagination", "page and per_page must be positive integers.", 400)

    pagination = User.query.order_by(User.id.asc()).paginate(
        page=page,
        per_page=min(per_page, 100),
        error_out=False,
    )

    return success_response(
        [user.to_dict() for user in pagination.items],
        meta={
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
        },
    )


@users_bp.patch("/users/<int:user_id>")
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
def delete_user(user_id: int):
    user = _get_user_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return no_content_response()
