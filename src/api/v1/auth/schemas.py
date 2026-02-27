from __future__ import annotations

from typing import Any

from core.errors import ValidationError


class AuthSchemas:
    @staticmethod
    def require_payload(payload: dict[str, Any] | None) -> dict[str, Any]:
        if not payload:
            raise ValidationError("Request body is required.")
        return payload

    @staticmethod
    def parse_email_password(payload: dict[str, Any] | None) -> tuple[str, str]:
        data = AuthSchemas.require_payload(payload)
        email = str(data.get("email", "")).strip().lower()
        password = str(data.get("password", ""))
        if not email or "@" not in email:
            raise ValidationError("A valid email is required.", {"field": "email"})
        if not password:
            raise ValidationError("password is required.", {"field": "password"})
        return email, password

    @staticmethod
    def parse_register(payload: dict[str, Any] | None) -> tuple[str, str, str]:
        email, password = AuthSchemas.parse_email_password(payload)
        full_name = str((payload or {}).get("full_name", "")).strip()
        if not full_name:
            raise ValidationError("full_name is required.", {"field": "full_name"})
        if len(password) < 8:
            raise ValidationError(
                "password must be at least 8 characters.",
                {"field": "password", "min_length": 8},
            )
        return email, full_name, password
