from flask import Flask
from flask_talisman import Talisman


def init_security_headers(app: Flask) -> None:
    if not app.config.get("ENABLE_SECURITY_HEADERS", True):
        return

    csp = {
        "default-src": ["'self'"],
        "script-src": ["'self'", "'unsafe-inline'", "https://cdn.tailwindcss.com"],
        "style-src": ["'self'", "'unsafe-inline'"],
        "img-src": ["'self'", "data:"],
        "font-src": ["'self'", "data:"],
    }

    Talisman(
        app,
        content_security_policy=csp,
        force_https=app.config.get("FORCE_HTTPS", False),
        strict_transport_security=app.config.get("ENABLE_HSTS", False),
    )
