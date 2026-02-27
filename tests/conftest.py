import os
import pytest
from app import create_app


@pytest.fixture()
def app():
    os.environ["FLASK_ENV"] = "testing"
    app = create_app("testing")
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
