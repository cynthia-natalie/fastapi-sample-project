import json
import os
from fastapi import FastAPI, Header, HTTPException
from typing import Annotated, Literal, Optional
from uuid import uuid4
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


fake_secret_token = "coneofsilence"

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

class Item(BaseModel):
    id: str
    title: str
    description: str | None = None

class Book(BaseModel):
    name: str
    genre: Literal["fiction", "non-fiction"]
    price: float
    book_id: Optional[str] = uuid4().hex


BOOKS_FILE = "books.json"
BOOKS = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOKS = json.load(f)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=409, detail="Item already exists")
    fake_db[item.id] = item
    return item

@app.get("/random-book")
async def random_book():
    return random.choice(BOOKS)

@app.get("/list-books")
async def list_books():
    return {"books": BOOKS}

@app.get("/book_by_index/{index}")
async def book_by_index(index: int):
    if index < len(BOOKS):
        return BOOKS[index]
    else:
        raise HTTPException(404, f"Book index {index} out of range ({len(BOOKS)}).")

@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOKS.append(json_book)

    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOKS, f)

    return {"book_id": book.book_id}

@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOKS:
        if book["book_id"] == book_id:
            return book

    raise HTTPException(404, f"Book ID {book_id} not found in database.")


# items = {"foo": {"name": "Foo", "description": "A test item"}}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items[item_id]

# @app.post("/items/{item_id}")
# async def create_item(item_id: str, item: dict):
#     if item_id in items:
#         raise HTTPException(status_code=400, detail="Item already exists")
#     items[item_id] = item
#     return item