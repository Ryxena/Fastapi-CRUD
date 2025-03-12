from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"message": f"Item ID requested: {item_id}"}

@app.get("/search/")
def search_items(query: str, limit: int = 10):
    return {"query": query, "limit": limit, "message": "Search results"}

@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully!",
        "item": item
    }