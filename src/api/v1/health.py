from flask import Blueprint

from core.responses import ok

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    return ok({"status": "ok"})
