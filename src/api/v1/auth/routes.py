from __future__ import annotations

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from core.authz import require_auth
from core.responses import created, ok

from .schemas import AuthSchemas
from .service import login_user, me, refresh_access_token, register_user, revoke_current_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/auth/register")
def register():
    email, full_name, password = AuthSchemas.parse_register(request.get_json(silent=True))
    return created(register_user(email, full_name, password))


@auth_bp.post("/auth/login")
def login():
    email, password = AuthSchemas.parse_email_password(request.get_json(silent=True))
    return ok(login_user(email, password))


@auth_bp.post("/auth/refresh")
@jwt_required(refresh=True)
def refresh():
    return ok(refresh_access_token())


@auth_bp.post("/auth/logout")
@jwt_required()
def logout():
    return ok(revoke_current_token())


@auth_bp.get("/auth/me")
@require_auth
def current_user_profile():
    return ok(me())
