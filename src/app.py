from flask import Flask

from api.health import health_bp
from api.users import users_bp
from config import get_config
from core.errors import register_error_handlers
from core.logging import configure_logging
from extensions.cors import init_cors
from extensions.db import db
from extensions.jwt import init_jwt
from extensions.migrate import migrate


def create_app(config_name: str | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    configure_logging(app)
    db.init_app(app)
    migrate.init_app(app, db)
    init_jwt(app)
    init_cors(app)

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(users_bp, url_prefix="/api")
    register_error_handlers(app)

    return app
