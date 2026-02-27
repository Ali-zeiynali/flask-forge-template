from app import create_app


def test_landing_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Flask Forge Template" in response.get_data(as_text=True)


def test_security_headers_enabled_in_production():
    app = create_app("production")
    with app.test_client() as test_client:
        response = test_client.get("/", base_url="https://localhost")

    assert response.status_code == 200
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Strict-Transport-Security"]
