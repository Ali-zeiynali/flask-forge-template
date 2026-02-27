from __future__ import annotations

from flask import Blueprint, request

from core.authz import require_owner_or_permission, require_permissions
from core.responses import created, no_content, ok, paginated

from .schemas import UserSchemas
from .service import create_user, delete_user, get_user, list_users, update_user

users_bp = Blueprint("users", __name__)


@users_bp.post("/users")
@require_permissions("users:write")
def create_user_route():
    email, full_name, password, is_active = UserSchemas.parse_create(request.get_json(silent=True))
    return created(create_user(email, full_name, password, is_active))


@users_bp.get("/users/<int:user_id>")
@require_owner_or_permission("users:read")
def get_user_route(user_id: int):
    return ok(get_user(user_id).to_dict())


@users_bp.get("/users")
@require_permissions("users:read")
def list_users_route():
    page = request.args.get("page", default=1, type=int)
    page_size = request.args.get(
        "page_size",
        request.args.get("per_page", default=10, type=int),
        type=int,
    )
    users, meta = list_users(page, page_size)
    return paginated(
        users,
        page=meta["page"],
        page_size=meta["page_size"],
        total=meta["total"],
        has_next=meta["has_next"],
    )


@users_bp.patch("/users/<int:user_id>")
@require_owner_or_permission("users:write")
def update_user_route(user_id: int):
    updates = UserSchemas.parse_patch(request.get_json(silent=True))
    return ok(update_user(user_id, updates))


@users_bp.delete("/users/<int:user_id>")
@require_permissions("users:write")
def delete_user_route(user_id: int):
    delete_user(user_id)
    return no_content()
