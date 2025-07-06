from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_auth_token():
    signup_data = {
        "email": "reporter@example.com",
        "password": "testpass",
        "role": "REPORTER"
    }
    client.post("/api/auth/signup", json=signup_data)
    login_data = {"email": signup_data["email"], "password": signup_data["password"]}
    res = client.post("/api/auth/login", json=login_data)
    return res.json()["access_token"]

def test_create_and_get_issues():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    issue_data = {
        "title": "Test Issue",
        "description": "This is a test",
        "severity": "HIGH"
    }
    res = client.post("/api/issues/", json=issue_data, headers=headers)
    assert res.status_code == 200
    issue_id = res.json()["id"]

    res = client.get("/api/issues/", headers=headers)
    assert res.status_code == 200
    assert any(i["id"] == issue_id for i in res.json())
