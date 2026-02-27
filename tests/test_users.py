def test_users_crud_flow(client, admin_headers):
    create_response = client.post(
        "/api/users",
        headers=admin_headers,
        json={"email": "first@example.com", "full_name": "First User", "password": "Password123"},
    )
    assert create_response.status_code == 201
    created_data = create_response.get_json()["data"]
    user_id = created_data["id"]
    assert created_data["email"] == "first@example.com"

    get_response = client.get(f"/api/users/{user_id}", headers=admin_headers)
    assert get_response.status_code == 200
    assert get_response.get_json()["data"]["full_name"] == "First User"

    list_response = client.get("/api/users?page=1&page_size=5", headers=admin_headers)
    assert list_response.status_code == 200
    payload = list_response.get_json()
    assert payload["meta"]["page"] == 1
    assert payload["meta"]["page_size"] == 5
    assert payload["meta"]["total"] >= 1

    patch_response = client.patch(
        f"/api/users/{user_id}",
        headers=admin_headers,
        json={"full_name": "Updated User", "is_active": False},
    )
    assert patch_response.status_code == 200
    updated = patch_response.get_json()["data"]
    assert updated["full_name"] == "Updated User"
    assert updated["is_active"] is False

    delete_response = client.delete(f"/api/users/{user_id}", headers=admin_headers)
    assert delete_response.status_code == 204

    get_after_delete = client.get(f"/api/users/{user_id}", headers=admin_headers)
    assert get_after_delete.status_code == 404


def test_users_permission_and_error_cases(client, admin_headers, user_headers):
    forbidden_create = client.post(
        "/api/users",
        headers=user_headers,
        json={"email": "bad@example.com", "full_name": "Bad", "password": "Password123"},
    )
    assert forbidden_create.status_code == 403

    invalid_create = client.post(
        "/api/users",
        headers=admin_headers,
        json={"email": "bad", "full_name": "", "password": "short"},
    )
    assert invalid_create.status_code == 400

    first_create = client.post(
        "/api/users",
        headers=admin_headers,
        json={"email": "duplicate@example.com", "full_name": "Name", "password": "Password123"},
    )
    assert first_create.status_code == 201

    duplicate_create = client.post(
        "/api/users",
        headers=admin_headers,
        json={"email": "duplicate@example.com", "full_name": "Name 2", "password": "Password123"},
    )
    assert duplicate_create.status_code == 409

    invalid_patch = client.patch("/api/users/1", headers=admin_headers, json={"is_active": "yes"})
    assert invalid_patch.status_code == 400

    invalid_pagination = client.get("/api/users?page=0&page_size=10", headers=admin_headers)
    assert invalid_pagination.status_code == 400


def test_regular_user_can_update_self_only(client, users, user_headers):
    own_update = client.patch(
        f"/api/users/{users['user'].id}",
        headers=user_headers,
        json={"full_name": "Self Updated"},
    )
    assert own_update.status_code == 200
    assert own_update.get_json()["data"]["full_name"] == "Self Updated"

    other_update = client.patch(
        f"/api/users/{users['admin'].id}",
        headers=user_headers,
        json={"full_name": "Nope"},
    )
    assert other_update.status_code == 403
