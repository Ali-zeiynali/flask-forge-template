from __future__ import annotations

from core.errors import ConflictError, NotFoundError, ValidationError
from core.security import hash_password
from models import User

from . import repo


def create_user(email: str, full_name: str, password: str, is_active: bool) -> dict[str, object]:
    if repo.find_by_email(email) is not None:
        raise ConflictError("User with this email already exists.")
    user = User(
        email=email,
        full_name=full_name,
        password_hash=hash_password(password),
        is_active=is_active,
    )
    return repo.save(user).to_dict()


def get_user(user_id: int) -> User:
    user = repo.find_by_id(user_id)
    if user is None:
        raise NotFoundError("User not found.")
    return user


def list_users(page: int, page_size: int) -> tuple[list[dict[str, object]], dict[str, int | bool]]:
    if page < 1 or page_size < 1:
        raise ValidationError("page and page_size must be positive integers.")
    pagination = repo.list_paginated(page, min(page_size, 100))
    return (
        [user.to_dict() for user in pagination.items],
        {
            "page": pagination.page,
            "page_size": pagination.per_page,
            "total": pagination.total,
            "has_next": pagination.has_next,
        },
    )


def update_user(user_id: int, updates: dict[str, object]) -> dict[str, object]:
    user = get_user(user_id)
    if "email" in updates:
        existing = User.query.filter(User.email == updates["email"], User.id != user.id).first()
        if existing is not None:
            raise ConflictError("User with this email already exists.")
    for field_name, value in updates.items():
        setattr(user, field_name, value)
    return repo.save(user).to_dict()


def delete_user(user_id: int) -> None:
    repo.delete(get_user(user_id))
