from __future__ import annotations

from models import User


def get_user(user_id: int) -> User | None:
    return User.query.filter_by(id=user_id).first()
