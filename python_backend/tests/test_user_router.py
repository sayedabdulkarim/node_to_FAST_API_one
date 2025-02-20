from fastapi.testclient import TestClient
import pytest
from ..app.main import app
from ..app.config.database import db

client = TestClient(app)

@pytest.fixture
async def cleanup_database():
    yield
    await db.users.delete_many({})

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == {"message": "Users endpoint"}

def test_user_signup(cleanup_database):
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1234567890"
    }
    response = client.post("/users/signup", json=test_user)
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"
    assert "token" in response.json()
    assert response.json()["user"]["email"] == test_user["email"]

def test_user_login(cleanup_database):
    # First create a user
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1234567890"
    }
    client.post("/users/signup", json=test_user)
    
    # Then try to login
    login_data = {
        "phone": "1234567890"
    }
    response = client.post("/users/login", json=login_data)
    assert response.status_code == 200
    assert "token" in response.json()
    assert response.json()["message"] == "Login successful"

def test_get_profile():
    # First create and login a user
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1234567890"
    }
    signup_response = client.post("/users/signup", json=test_user)
    token = signup_response.json()["token"]
    
    # Test profile endpoint
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/profile", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == test_user["email"]

def test_update_profile():
    # First create and login a user
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1234567890"
    }
    signup_response = client.post("/users/signup", json=test_user)
    token = signup_response.json()["token"]
    
    # Update profile
    update_data = {
        "name": "Updated Name",
        "email": "updated@example.com"
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/users/profile", json=update_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == update_data["name"]
    assert response.json()["email"] == update_data["email"]
