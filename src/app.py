from flask import Flask
from config import get_config
from core.logging import configure_logging
from extensions.db import db
from extensions.migrate import migrate
from api.health import health_bp


def create_app(config_name: str | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    configure_logging(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(health_bp, url_prefix="/api")

    return app