import os


class BaseConfig:
    APP_NAME = os.getenv("APP_NAME", "flask-forge-template")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-super-secret-key-please-replace")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
    RATE_LIMIT_LOGIN_PER_MINUTE = int(os.getenv("RATE_LIMIT_LOGIN_PER_MINUTE", "10"))
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "3600"))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "2592000"))
    ENABLE_SECURITY_HEADERS = os.getenv("ENABLE_SECURITY_HEADERS", "true").lower() == "true"
    ENABLE_HSTS = os.getenv("ENABLE_HSTS", "false").lower() == "true"
    FORCE_HTTPS = os.getenv("FORCE_HTTPS", "false").lower() == "true"
    DOCS_URL = os.getenv("DOCS_URL", "/docs/index.md")
    GITHUB_URL = os.getenv("GITHUB_URL", "https://github.com/example/flask-forge-template")
    CI_STATUS = os.getenv("CI_STATUS", "Passing")


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    RATE_LIMIT_LOGIN_PER_MINUTE = 1000
    ENABLE_SECURITY_HEADERS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    FLASK_ENV = "production"
    ENABLE_HSTS = True
    FORCE_HTTPS = True


def get_config(name: str | None):
    value = (name or os.getenv("FLASK_ENV") or "development").lower()

    if value in {"test", "testing"}:
        return TestingConfig
    if value in {"prod", "production"}:
        return ProductionConfig
    return DevelopmentConfig
