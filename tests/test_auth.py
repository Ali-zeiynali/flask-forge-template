def test_register_login_refresh_me_logout_flow(client):
    register_response = client.post(
        "/api/auth/register",
        json={
            "email": "new@example.com",
            "full_name": "New User",
            "password": "Password123",
        },
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/api/auth/login",
        json={"email": "new@example.com", "password": "Password123"},
    )
    assert login_response.status_code == 200
    tokens = login_response.get_json()["data"]

    me_response = client.get(
        "/api/auth/me", headers={"Authorization": f"Bearer {tokens['access_token']}"}
    )
    assert me_response.status_code == 200
    assert me_response.get_json()["data"]["email"] == "new@example.com"

    refresh_response = client.post(
        "/api/auth/refresh", headers={"Authorization": f"Bearer {tokens['refresh_token']}"}
    )
    assert refresh_response.status_code == 200
    assert "access_token" in refresh_response.get_json()["data"]

    logout_response = client.post(
        "/api/auth/logout", headers={"Authorization": f"Bearer {tokens['access_token']}"}
    )
    assert logout_response.status_code == 200

    me_after_logout = client.get(
        "/api/auth/me", headers={"Authorization": f"Bearer {tokens['access_token']}"}
    )
    assert me_after_logout.status_code == 401


def test_auth_errors_and_invalid_token(client):
    invalid_payload = client.post("/api/auth/register", json={"email": "bad", "password": "123"})
    assert invalid_payload.status_code == 400

    conflict = client.post(
        "/api/auth/register",
        json={
            "email": "dup@example.com",
            "full_name": "Dup",
            "password": "Password123",
        },
    )
    assert conflict.status_code == 201

    conflict_again = client.post(
        "/api/auth/register",
        json={
            "email": "dup@example.com",
            "full_name": "Dup 2",
            "password": "Password123",
        },
    )
    assert conflict_again.status_code == 409

    bad_login = client.post(
        "/api/auth/login",
        json={"email": "dup@example.com", "password": "WrongPass"},
    )
    assert bad_login.status_code == 401

    invalid_token = client.get("/api/auth/me", headers={"Authorization": "Bearer invalid"})
    assert invalid_token.status_code == 401
