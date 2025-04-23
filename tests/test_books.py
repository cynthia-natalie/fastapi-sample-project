import json
import os
import pytest
from fastapi.testclient import TestClient
from app.main import root, BOOKS_FILE, BOOKS, Book

client = TestClient(root)

test_books = [
    {"name": "Book One", "genre": "fiction", "price": 10.99, "book_id": "1"},
    {"name": "Book Two", "genre": "non-fiction", "price": 15.99, "book_id": "2"},
]

@pytest.fixture(scope="function", autouse=True)
def setup_books():
    BOOKS.clear()
    BOOKS.extend(test_books)
    
    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOKS, f)
    
    yield
    
    os.remove(BOOKS_FILE)

def test_list_books():
    response = client.get("/list-books")
    assert response.status_code == 200
    assert len(response.json()["books"]) == 2

def test_random_book():
    response = client.get("/random-book")
    assert response.status_code == 200
    assert response.json()["name"] in ["Book One", "Book Two"]

def test_book_by_index_valid():
    response = client.get("/book_by_index/0")
    assert response.status_code == 200
    assert response.json()["name"] == "Book One"

def test_book_by_index_out_of_range():
    response = client.get("/book_by_index/5")
    assert response.status_code == 404
    assert "Book index 5 out of range" in response.json()["detail"]

def test_add_book():
    new_book = {"name": "Book Three", "genre": "fiction", "price": 20.99}
    response = client.post("/add-book", json=new_book)
    assert response.status_code == 200
    assert "book_id" in response.json()

    response = client.get("/list-books")
    assert len(response.json()["books"]) == 3

def test_get_book_found():
    response = client.get("/get-book", params={"book_id": "1"})
    assert response.status_code == 200
    assert response.json()["name"] == "Book One"

def test_get_book_not_found():
    response = client.get("/get-book", params={"book_id": "999"})
    assert response.status_code == 404
    assert "Book ID 999 not found" in response.json()["detail"]
