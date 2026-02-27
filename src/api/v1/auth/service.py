from __future__ import annotations

from models import User


def normalize_email(email: str) -> str:
    return email.strip().lower()


def is_email_taken(email: str) -> bool:
    return User.query.filter_by(email=normalize_email(email)).first() is not None
