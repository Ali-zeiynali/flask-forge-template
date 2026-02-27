from __future__ import annotations

from datetime import UTC, datetime

from flask import Flask
from flask_jwt_extended import JWTManager

from core.responses import error_response

jwt = JWTManager()
TOKEN_BLOCKLIST: dict[str, float] = {}


def init_jwt(app: Flask) -> None:
    jwt.init_app(app)

    @jwt.token_in_blocklist_loader
    def is_token_revoked(_header, jwt_payload):
        jti = jwt_payload["jti"]
        expires_at = TOKEN_BLOCKLIST.get(jti)
        if expires_at is None:
            return False
        now = datetime.now(UTC).timestamp()
        if now > expires_at:
            TOKEN_BLOCKLIST.pop(jti, None)
            return False
        return True

    @jwt.unauthorized_loader
    def unauthorized_callback(message: str):
        return error_response("auth_missing", message, 401)

    @jwt.invalid_token_loader
    def invalid_callback(message: str):
        return error_response("auth_invalid_token", message, 401)

    @jwt.expired_token_loader
    def expired_callback(_header, _payload):
        return error_response("auth_token_expired", "Token has expired.", 401)

    @jwt.revoked_token_loader
    def revoked_callback(_header, _payload):
        return error_response("auth_token_revoked", "Token has been revoked.", 401)
