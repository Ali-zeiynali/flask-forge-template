from __future__ import annotations

import os
from typing import Any


def get_env(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)


def get_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    return int(value)


def get_csv(name: str, default: str = "") -> list[str] | str:
    raw = os.getenv(name, default).strip()
    if raw == "*":
        return "*"
    return [item.strip() for item in raw.split(",") if item.strip()]


def safe_config_snapshot(config: dict[str, Any]) -> dict[str, Any]:
    redacted = {"SECRET_KEY", "JWT_SECRET_KEY", "SQLALCHEMY_DATABASE_URI"}
    data: dict[str, Any] = {}
    for key in sorted(config):
        if key in redacted:
            data[key] = "***"
        elif key.startswith("JWT") or key in {
            "APP_ENV",
            "LOG_LEVEL",
            "RATE_LIMIT_ENABLED",
            "SECURITY_HEADERS_ENABLED",
        }:
            data[key] = config[key]
    return data
