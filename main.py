from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

#Path params
@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict:
    return {"message": f"Item ID requested: {item_id}"}

#Queryy params
@app.get("/search/")
def search_items(query: str, limit: int = 10) -> dict:
    return {"query": query, "limit": limit, "message": "Search results"}

#Post data body
@app.post("/items/")
def create_item(item: Item) -> dict:
    return {
        "message": "Item created successfully!",
        "item": item
    }

#Query + Path Params
@app.get('/halo/{nama}')
def nama(nama: str,   age: int) -> dict:
    return {
        "nama": nama,
        "umur": age
    }


@app.get('/user')
def get_user(user: Optional["str"] = "User") -> dict:
    return {
        "data": {
            "username": user
        }
    }
