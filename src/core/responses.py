from __future__ import annotations

from typing import Any

from flask import jsonify


def success_response(data: Any, status_code: int = 200, meta: dict[str, Any] | None = None):
    payload: dict[str, Any] = {"success": True, "data": data}
    if meta is not None:
        payload["meta"] = meta
    return jsonify(payload), status_code


def created_response(data: Any):
    return success_response(data, status_code=201)


def no_content_response():
    return "", 204


def error_response(
    code: str, message: str, status_code: int, details: dict[str, Any] | None = None
):
    payload: dict[str, Any] = {
        "success": False,
        "error": {
            "code": code,
            "message": message,
        },
    }
    if details:
        payload["error"]["details"] = details
    return jsonify(payload), status_code
