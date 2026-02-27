from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from werkzeug.exceptions import HTTPException

from core.responses import error_response


@dataclass
class APIError(Exception):
    code: str
    message: str
    status_code: int = 400
    details: dict[str, Any] | None = None


def register_error_handlers(app):
    @app.errorhandler(APIError)
    def handle_api_error(error: APIError):
        return error_response(error.code, error.message, error.status_code, error.details)

    @app.errorhandler(HTTPException)
    def handle_http_exception(error: HTTPException):
        return error_response("http_error", error.description, error.code or 500)

    @app.errorhandler(Exception)
    def handle_unexpected_error(_error: Exception):
        return error_response("internal_error", "Internal server error.", 500)
