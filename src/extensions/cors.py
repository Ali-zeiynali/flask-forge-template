from flask import Flask
from flask_cors import CORS


def init_cors(app: Flask) -> None:
    origins = app.config.get("CORS_ORIGINS", "*")
    CORS(app, resources={r"/api/*": {"origins": origins}})
