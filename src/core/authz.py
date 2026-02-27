from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any

from flask import g, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from core.errors import APIError
from extensions.db import db
from models import User


def require_auth(fn: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fn)
    @jwt_required()
    def wrapper(*args: Any, **kwargs: Any):
        identity = get_jwt_identity()
        user = db.session.get(User, int(identity))
        if user is None or not user.is_active:
            raise APIError("auth_invalid_user", "Authentication required.", 401)
        g.current_user = user
        return fn(*args, **kwargs)

    return wrapper


def require_roles(*roles: str):
    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fn)
        @require_auth
        def wrapper(*args: Any, **kwargs: Any):
            user = g.current_user
            if not any(user.has_role(role) for role in roles):
                raise APIError("forbidden_role", "Insufficient role.", 403)
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def require_permissions(*permissions: str):
    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fn)
        @require_auth
        def wrapper(*args: Any, **kwargs: Any):
            user = g.current_user
            missing = [
                permission for permission in permissions if not user.has_permission(permission)
            ]
            if missing:
                raise APIError(
                    "forbidden_permission",
                    "Insufficient permissions.",
                    403,
                    details={"missing": missing},
                )
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def require_owner_or_permission(permission: str, owner_param: str = "user_id"):
    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fn)
        @require_auth
        def wrapper(*args: Any, **kwargs: Any):
            user = g.current_user
            owner_id = kwargs.get(owner_param)
            if owner_id is None and owner_param in request.view_args:
                owner_id = request.view_args.get(owner_param)
            if owner_id == user.id or user.has_permission(permission):
                return fn(*args, **kwargs)
            raise APIError("forbidden_owner", "Resource access denied.", 403)

        return wrapper

    return decorator
