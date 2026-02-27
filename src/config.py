import os


class BaseConfig:
    APP_NAME = os.getenv("APP_NAME", "flask-forge-template")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(BaseConfig):
    DEBUG = False


def get_config(name: str | None):
    value = (name or os.getenv("FLASK_ENV") or "development").lower()

    if value in {"test", "testing"}:
        return TestingConfig
    if value in {"prod", "production"}:
        return ProductionConfig
    return DevelopmentConfig
