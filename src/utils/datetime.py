from datetime import UTC, datetime


def utcnow_iso() -> str:
    return datetime.now(UTC).isoformat()
