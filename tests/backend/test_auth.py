from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup_and_login():
    signup_data = {
        "email": "user@example.com",
        "password": "password123",
        "role": "REPORTER"
    }
    res = client.post("/api/auth/signup", json=signup_data)
    assert res.status_code == 200
    token = res.json()["access_token"]
    assert token

    login_data = {
        "email": "user@example.com",
        "password": "password123"
    }
    res = client.post("/api/auth/login", json=login_data)
    assert res.status_code == 200
    assert "access_token" in res.json()
