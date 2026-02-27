from __future__ import annotations

import logging
import time
import uuid

from flask import Flask, g, has_request_context, request

SENSITIVE_HEADERS = {"authorization", "cookie", "set-cookie"}


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
    logger = logging.getLogger()
    for handler in logger.handlers:
        handler.addFilter(RequestIdFilter())

    @app.before_request
    def add_request_id() -> None:
        g.request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        g.request_started_at = time.perf_counter()

    @app.after_request
    def log_request_response(response):
        started_at = getattr(g, "request_started_at", time.perf_counter())
        duration_ms = (time.perf_counter() - started_at) * 1000
        header_keys = [
            key for key in request.headers.keys() if key.lower() not in SENSITIVE_HEADERS
        ]
        app.logger.info(
            "%s %s -> %s (%.2fms) headers=%s",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
            header_keys,
        )
        response.headers["X-Request-ID"] = g.request_id
        return response
