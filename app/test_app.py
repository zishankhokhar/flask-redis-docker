from app import app

def test_welcome_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data