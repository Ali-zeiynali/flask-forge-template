import os


class BaseConfig:
    APP_NAME = os.getenv("APP_NAME", "flask-forge-template")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-super-secret-key-please-replace")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
    RATE_LIMIT_LOGIN_PER_MINUTE = int(os.getenv("RATE_LIMIT_LOGIN_PER_MINUTE", "10"))
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "3600"))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "2592000"))


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    RATE_LIMIT_LOGIN_PER_MINUTE = 1000


class ProductionConfig(BaseConfig):
    DEBUG = False


def get_config(name: str | None):
    value = (name or os.getenv("FLASK_ENV") or "development").lower()

    if value in {"test", "testing"}:
        return TestingConfig
    if value in {"prod", "production"}:
        return ProductionConfig
    return DevelopmentConfig
