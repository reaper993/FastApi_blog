def test_create_user(client):
    data = {"email": "ping@fastapiexample.com", "password": "supersecret"}
    response = client.post("/users/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "ping@fastapiexample.com"