from __future__ import annotations

from core.settings import get_bool, get_csv, get_env, get_int


class BaseConfig:
    APP_NAME = get_env("APP_NAME", "flask-forge-template")
    APP_VERSION = get_env("APP_VERSION", "0.1.0")
    APP_ENV = get_env("APP_ENV", get_env("FLASK_ENV", "development"))
    FLASK_ENV = APP_ENV

    SECRET_KEY = get_env("SECRET_KEY", "change-me-super-secret-key-please-replace")
    JWT_SECRET_KEY = get_env("JWT_SECRET_KEY", SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = get_env("DATABASE_URL", "sqlite:///./dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_ACCESS_TOKEN_EXPIRES = get_int(
        "JWT_ACCESS_EXPIRES", get_int("JWT_ACCESS_TOKEN_EXPIRES", 3600)
    )
    JWT_REFRESH_TOKEN_EXPIRES = get_int(
        "JWT_REFRESH_EXPIRES", get_int("JWT_REFRESH_TOKEN_EXPIRES", 2592000)
    )

    LOG_LEVEL = get_env("LOG_LEVEL", "INFO")
    CORS_ORIGINS = get_csv("CORS_ORIGINS", "*")
    RATE_LIMIT_ENABLED = get_bool("RATE_LIMIT_ENABLED", True)
    RATE_LIMIT_LOGIN_PER_MINUTE = get_int("RATE_LIMIT_LOGIN_PER_MINUTE", 10)
    SECURITY_HEADERS_ENABLED = get_bool("SECURITY_HEADERS_ENABLED", True)
    ADMIN_SEED_ENABLED = get_bool("ADMIN_SEED_ENABLED", True)

    ENABLE_SECURITY_HEADERS = SECURITY_HEADERS_ENABLED
    ENABLE_HSTS = get_bool("ENABLE_HSTS", False)
    FORCE_HTTPS = get_bool("FORCE_HTTPS", False)

    DOCS_URL = get_env("DOCS_URL", "/docs/index.md")
    GITHUB_URL = get_env("GITHUB_URL", "https://github.com/example/flask-forge-template")
    CI_STATUS = get_env("CI_STATUS", "Passing")


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    APP_ENV = "testing"
    FLASK_ENV = "testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    RATE_LIMIT_ENABLED = False
    RATE_LIMIT_LOGIN_PER_MINUTE = 1000
    SECURITY_HEADERS_ENABLED = False
    ENABLE_SECURITY_HEADERS = False
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    JWT_REFRESH_TOKEN_EXPIRES = 7200


class ProductionConfig(BaseConfig):
    DEBUG = False
    APP_ENV = "production"
    FLASK_ENV = "production"
    ENABLE_HSTS = True
    FORCE_HTTPS = True


def get_config(name: str | None):
    value = (
        name or get_env("APP_ENV", get_env("FLASK_ENV", "development")) or "development"
    ).lower()
    if value in {"test", "testing"}:
        return TestingConfig
    if value in {"prod", "production"}:
        return ProductionConfig
    return DevelopmentConfig
