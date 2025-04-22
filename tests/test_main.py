from fastapi.testclient import TestClient
from .app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }

def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

def test_read_nonexistent_item():
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }

def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Item already exists"}

# def test_read_item():
#     response = client.get("/items/foo")
#     assert response.status_code == 200
#     assert response.json() == {"name": "Foo", "description": "A test item"}

# def test_read_item_not_found():
#     response = client.get("/items/bar")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}

# def test_create_item():
#     new_item = {"name": "Bar", "description": "Another test item"}
#     response = client.post("/items/bar", json=new_item)
#     assert response.status_code == 200
#     assert response.json() == new_item

# def test_create_item_already_exists():
#     new_item = {"name": "Foo", "description": "Duplicate item"}
#     response = client.post("/items/foo", json=new_item)
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Item already exists"}
