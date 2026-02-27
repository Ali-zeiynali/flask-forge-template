from __future__ import annotations

from extensions.db import db
from models import User


def find_by_id(user_id: int) -> User | None:
    return db.session.get(User, user_id)


def find_by_email(email: str) -> User | None:
    return User.query.filter_by(email=email).first()


def list_paginated(page: int, page_size: int):
    return User.query.order_by(User.id.asc()).paginate(
        page=page, per_page=page_size, error_out=False
    )


def save(user: User) -> User:
    db.session.add(user)
    db.session.commit()
    return user


def delete(user: User) -> None:
    db.session.delete(user)
    db.session.commit()
