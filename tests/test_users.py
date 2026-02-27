def test_users_crud_flow(client):
    create_response = client.post(
        "/api/users",
        json={"email": "first@example.com", "full_name": "First User"},
    )
    assert create_response.status_code == 201
    created_data = create_response.get_json()["data"]
    user_id = created_data["id"]
    assert created_data["email"] == "first@example.com"

    get_response = client.get(f"/api/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.get_json()["data"]["full_name"] == "First User"

    list_response = client.get("/api/users?page=1&per_page=5")
    assert list_response.status_code == 200
    payload = list_response.get_json()
    assert payload["meta"]["page"] == 1
    assert payload["meta"]["per_page"] == 5
    assert payload["meta"]["total"] == 1

    patch_response = client.patch(
        f"/api/users/{user_id}",
        json={"full_name": "Updated User", "is_active": False},
    )
    assert patch_response.status_code == 200
    updated = patch_response.get_json()["data"]
    assert updated["full_name"] == "Updated User"
    assert updated["is_active"] is False

    delete_response = client.delete(f"/api/users/{user_id}")
    assert delete_response.status_code == 204

    get_after_delete = client.get(f"/api/users/{user_id}")
    assert get_after_delete.status_code == 404


def test_users_error_cases(client):
    invalid_create = client.post("/api/users", json={"email": "bad", "full_name": ""})
    assert invalid_create.status_code == 400

    first_create = client.post(
        "/api/users",
        json={"email": "duplicate@example.com", "full_name": "Name"},
    )
    assert first_create.status_code == 201

    duplicate_create = client.post(
        "/api/users",
        json={"email": "duplicate@example.com", "full_name": "Name 2"},
    )
    assert duplicate_create.status_code == 409

    invalid_patch = client.patch("/api/users/1", json={"is_active": "yes"})
    assert invalid_patch.status_code == 400

    invalid_pagination = client.get("/api/users?page=0&per_page=10")
    assert invalid_pagination.status_code == 400
