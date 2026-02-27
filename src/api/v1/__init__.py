from api.v1.admin.routes import admin_bp
from api.v1.auth.routes import auth_bp
from api.v1.health import health_bp
from api.v1.users.routes import users_bp

__all__ = ["admin_bp", "auth_bp", "health_bp", "users_bp"]
