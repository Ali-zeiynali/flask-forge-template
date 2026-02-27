from __future__ import annotations

from typing import Any

from flask import jsonify


def ok(data: Any, meta: dict[str, Any] | None = None, status_code: int = 200):
    payload: dict[str, Any] = {"data": data}
    if meta is not None:
        payload["meta"] = meta
    return jsonify(payload), status_code


def created(data: Any):
    return ok(data, status_code=201)


def no_content():
    return "", 204


def paginated(data: Any, *, page: int, page_size: int, total: int, has_next: bool):
    return ok(
        data,
        meta={
            "page": page,
            "page_size": page_size,
            "total": total,
            "has_next": has_next,
        },
    )


def error_response(
    code: str, message: str, status_code: int, details: dict[str, Any] | None = None
):
    payload: dict[str, Any] = {"error": {"code": code, "message": message, "details": details}}
    return jsonify(payload), status_code


# Backward-compatible aliases
success_response = ok
created_response = created
no_content_response = no_content
