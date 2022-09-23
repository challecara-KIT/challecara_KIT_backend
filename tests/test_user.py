from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_create_user():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
