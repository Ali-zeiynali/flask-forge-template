def test_admin_role_permission_management(client, admin_headers):
    create_permission = client.post(
        "/api/admin/permissions",
        headers=admin_headers,
        json={"name": "reports:read", "description": "Read reports"},
    )
    assert create_permission.status_code == 201

    create_role = client.post(
        "/api/admin/roles",
        headers=admin_headers,
        json={"name": "auditor", "description": "Audits"},
    )
    assert create_role.status_code == 201
    role_id = create_role.get_json()["data"]["id"]

    patch_role = client.patch(
        f"/api/admin/roles/{role_id}",
        headers=admin_headers,
        json={"description": "Audit team"},
    )
    assert patch_role.status_code == 200

    list_roles = client.get("/api/admin/roles", headers=admin_headers)
    assert list_roles.status_code == 200


def test_non_admin_forbidden(client, user_headers, users, admin_headers):
    _ = admin_headers
    forbidden = client.get("/api/admin/roles", headers=user_headers)
    assert forbidden.status_code == 403

    assign = client.post(
        f"/api/admin/users/{users['user'].id}/roles",
        headers=admin_headers,
        json={"name": "staff", "action": "assign"},
    )
    assert assign.status_code == 200

    remove = client.post(
        f"/api/admin/users/{users['user'].id}/roles",
        headers=admin_headers,
        json={"name": "staff", "action": "remove"},
    )
    assert remove.status_code == 200
