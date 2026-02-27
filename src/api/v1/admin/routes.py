from __future__ import annotations

from typing import Any

from flask import Blueprint, request

from core.authz import require_roles
from core.errors import APIError, ConflictError, NotFoundError, ValidationError
from core.responses import created, no_content, ok
from extensions.db import db
from models import Permission, Role, User

admin_bp = Blueprint("admin", __name__)


def _required_name(payload: dict[str, Any] | None) -> str:
    name = str((payload or {}).get("name", "")).strip()
    if not name:
        raise ValidationError("name is required.", {"field": "name"})
    return name


@admin_bp.get("/admin/roles")
@require_roles("admin")
def list_roles():
    return ok([role.to_dict() for role in Role.query.order_by(Role.id.asc()).all()])


@admin_bp.post("/admin/roles")
@require_roles("admin")
def create_role():
    payload = request.get_json(silent=True)
    name = _required_name(payload)
    if Role.query.filter_by(name=name).first() is not None:
        raise ConflictError("Role already exists.")
    role = Role(name=name, description=(payload or {}).get("description"))
    db.session.add(role)
    db.session.commit()
    return created(role.to_dict())


@admin_bp.patch("/admin/roles/<int:role_id>")
@require_roles("admin")
def patch_role(role_id: int):
    role = db.session.get(Role, role_id)
    if role is None:
        raise NotFoundError("Role not found.")
    payload = request.get_json(silent=True) or {}
    if "name" in payload:
        role.name = _required_name(payload)
    if "description" in payload:
        role.description = payload["description"]
    db.session.commit()
    return ok(role.to_dict())


@admin_bp.delete("/admin/roles/<int:role_id>")
@require_roles("admin")
def delete_role(role_id: int):
    role = db.session.get(Role, role_id)
    if role is None:
        raise NotFoundError("Role not found.")
    db.session.delete(role)
    db.session.commit()
    return no_content()


@admin_bp.get("/admin/permissions")
@require_roles("admin")
def list_permissions():
    return ok([item.to_dict() for item in Permission.query.order_by(Permission.id.asc()).all()])


@admin_bp.post("/admin/permissions")
@require_roles("admin")
def create_permission():
    payload = request.get_json(silent=True)
    name = _required_name(payload)
    if Permission.query.filter_by(name=name).first() is not None:
        raise ConflictError("Permission already exists.")
    item = Permission(name=name, description=(payload or {}).get("description"))
    db.session.add(item)
    db.session.commit()
    return created(item.to_dict())


@admin_bp.patch("/admin/permissions/<int:permission_id>")
@require_roles("admin")
def patch_permission(permission_id: int):
    item = db.session.get(Permission, permission_id)
    if item is None:
        raise NotFoundError("Permission not found.")
    payload = request.get_json(silent=True) or {}
    if "name" in payload:
        item.name = _required_name(payload)
    if "description" in payload:
        item.description = payload["description"]
    db.session.commit()
    return ok(item.to_dict())


@admin_bp.delete("/admin/permissions/<int:permission_id>")
@require_roles("admin")
def delete_permission(permission_id: int):
    item = db.session.get(Permission, permission_id)
    if item is None:
        raise NotFoundError("Permission not found.")
    db.session.delete(item)
    db.session.commit()
    return no_content()


@admin_bp.post("/admin/users/<int:user_id>/roles")
@require_roles("admin")
def assign_or_remove_roles(user_id: int):
    user = db.session.get(User, user_id)
    if user is None:
        raise NotFoundError("User not found.")
    payload = request.get_json(silent=True) or {}
    role_name = _required_name(payload)
    action = str(payload.get("action", "assign")).lower()
    role = Role.query.filter_by(name=role_name).first()
    if role is None:
        raise NotFoundError("Role not found.")
    if action == "assign":
        if role not in user.roles:
            user.roles.append(role)
    elif action == "remove":
        if role in user.roles:
            user.roles.remove(role)
    else:
        raise APIError("invalid_action", "action must be assign or remove.", 400)
    db.session.commit()
    return ok(user.to_dict())


@admin_bp.post("/admin/roles/<int:role_id>/permissions")
@require_roles("admin")
def assign_or_remove_permissions(role_id: int):
    role = db.session.get(Role, role_id)
    if role is None:
        raise NotFoundError("Role not found.")
    payload = request.get_json(silent=True) or {}
    permission_name = _required_name(payload)
    action = str(payload.get("action", "assign")).lower()
    permission = Permission.query.filter_by(name=permission_name).first()
    if permission is None:
        raise NotFoundError("Permission not found.")
    if action == "assign":
        if permission not in role.permissions:
            role.permissions.append(permission)
    elif action == "remove":
        if permission in role.permissions:
            role.permissions.remove(permission)
    else:
        raise APIError("invalid_action", "action must be assign or remove.", 400)
    db.session.commit()
    return ok(role.to_dict())
