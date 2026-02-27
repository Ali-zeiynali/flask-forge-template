from __future__ import annotations

import logging
import uuid

from flask import Flask, g, has_request_context, request


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = getattr(g, "request_id", "-") if has_request_context() else "-"
        return True


def configure_logging(app: Flask) -> None:
    level_name = app.config.get("LOG_LEVEL", "INFO")
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s [%(request_id)s] %(name)s: %(message)s",
    )
    for handler in logging.getLogger().handlers:
        handler.addFilter(RequestIdFilter())

    @app.before_request
    def add_request_id() -> None:
        g.request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
