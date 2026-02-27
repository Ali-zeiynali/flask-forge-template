from flask import Flask

import models  # noqa: F401
from api.admin import admin_bp
from api.auth import auth_bp
from api.health import health_bp
from api.users import users_bp
from cli import register_cli_commands
from config import get_config
from core.errors import register_error_handlers
from core.logging import configure_logging
from extensions.cors import init_cors
from extensions.db import db
from extensions.jwt import init_jwt
from extensions.migrate import migrate
from extensions.security_headers import init_security_headers
from web import web_bp


def create_app(config_name: str | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    configure_logging(app)
    db.init_app(app)
    migrate.init_app(app, db)
    init_jwt(app)
    init_cors(app)
    init_security_headers(app)

    app.register_blueprint(web_bp)
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(health_bp, url_prefix="/api/v1", name="health_v1")
    app.register_blueprint(users_bp, url_prefix="/api")
    app.register_blueprint(users_bp, url_prefix="/api/v1", name="users_v1")
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api/v1", name="auth_v1")
    app.register_blueprint(admin_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/v1", name="admin_v1")
    register_error_handlers(app)
    register_cli_commands(app)

    return app
