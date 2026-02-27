from __future__ import annotations

from typing import Any

from core.errors import ValidationError


class UserSchemas:
    @staticmethod
    def parse_create(payload: dict[str, Any] | None) -> tuple[str, str, str, bool]:
        if not payload:
            raise ValidationError("Request body is required.")

        email = str(payload.get("email", "")).strip().lower()
        full_name = str(payload.get("full_name", "")).strip()
        password = str(payload.get("password", "")).strip()
        is_active = payload.get("is_active", True)

        if not email or "@" not in email:
            raise ValidationError("A valid email is required.", {"field": "email"})
        if not full_name:
            raise ValidationError("full_name is required.", {"field": "full_name"})
        if not password or len(password) < 8:
            raise ValidationError(
                "password must be at least 8 characters.",
                {"field": "password", "min_length": 8},
            )
        if not isinstance(is_active, bool):
            raise ValidationError("is_active must be a boolean.", {"field": "is_active"})

        return email, full_name, password, is_active

    @staticmethod
    def parse_patch(payload: dict[str, Any] | None) -> dict[str, Any]:
        if not payload:
            raise ValidationError("Request body is required.")

        allowed_keys = {"email", "full_name", "is_active"}
        invalid_keys = set(payload) - allowed_keys
        if invalid_keys:
            raise ValidationError(
                "Unsupported fields were provided.", {"fields": sorted(invalid_keys)}
            )

        updates: dict[str, Any] = {}
        if "email" in payload:
            email = str(payload["email"]).strip().lower()
            if not email or "@" not in email:
                raise ValidationError("A valid email is required.", {"field": "email"})
            updates["email"] = email
        if "full_name" in payload:
            full_name = str(payload["full_name"]).strip()
            if not full_name:
                raise ValidationError("full_name cannot be empty.", {"field": "full_name"})
            updates["full_name"] = full_name
        if "is_active" in payload:
            if not isinstance(payload["is_active"], bool):
                raise ValidationError("is_active must be a boolean.", {"field": "is_active"})
            updates["is_active"] = payload["is_active"]
        if not updates:
            raise ValidationError("At least one valid field must be provided.")
        return updates
