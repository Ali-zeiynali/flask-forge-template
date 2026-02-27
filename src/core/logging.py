import logging
from flask import Flask


def configure_logging(app: Flask) -> None:
    level_name = app.config.get("LOG_LEVEL", "INFO")
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(level=level)
