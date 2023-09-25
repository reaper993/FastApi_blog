from fastapi.testclient import TestClient
from dependency_injection_2 import app, get_db_session

test_db = ["Database for testing"]

def get_testing_db():
    return test_db

app.dependency_overrides[get_db_session] = get_testing_db
client = TestClient(app)

def test_item_should_add_to_database():
    response = client.post("/items/?item=sugar")
    assert response.status_code == 200
    assert response.text == '{"message":"Added item: sugar"}'