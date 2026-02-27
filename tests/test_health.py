def test_health_alias_and_v1(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"data": {"status": "ok"}}

    v1_response = client.get("/api/v1/health")
    assert v1_response.status_code == 200
    assert v1_response.get_json() == {"data": {"status": "ok"}}
