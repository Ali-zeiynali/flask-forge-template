from api.admin import admin_bp
from api.auth import auth_bp
from api.health import health_bp
from api.users import users_bp

__all__ = ["admin_bp", "auth_bp", "health_bp", "users_bp"]
