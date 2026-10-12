import re

from app import app


def get_visits(client):
    response = client.get("/count")
    assert response.status_code == 200
    match = re.search(r"visited (\d+) times", response.get_data(as_text=True))
    assert match
    return int(match.group(1))


def test_welcome_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_count_increments():
    client = app.test_client()
    first = get_visits(client)
    second = get_visits(client)
    assert second == first + 1
