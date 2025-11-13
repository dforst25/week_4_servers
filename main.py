from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from utils.json_handler import *


class Item(BaseModel):
    id: int
    name: str
    price: float


app = FastAPI()


@app.get("/test")
def response():
    pass

JSON_PATH = "./data/data.json"


@app.put("/items/{item_id}")
def update_price(item_id: int, new_price: float):
    items = JsonHandler.load_data(JSON_PATH)
    for item in items:
        if item['id'] == item_id:
            item['price'] = new_price
            JsonHandler.save_data(items, JSON_PATH)
            return item
    raise HTTPException(status_code=404, detail="item not found")


@app.post("/items/")
def add_item(new_item: Item):
    items = JsonHandler.load_data(JSON_PATH)
    for item in items:
        if item['id'] == new_item.id:
            raise HTTPException(status_code=409, detail="Item already exists")
    items.append(new_item.dict())
    JsonHandler.save_data(items, JSON_PATH)
    return new_item.dict()


def get_sort_key(item, sort_by):
    value = item[sort_by]
    if isinstance(value, str):
        return value.lower()
    return value


@app.get("/items/")
def get_sorted_items(sort_alg: str = "asc", sort_by: str = None):
    items = JsonHandler.load_data(JSON_PATH)
    if not sort_by:
        return items
    items.sort(key=lambda item: get_sort_key(item, sort_by), reverse=(sort_alg == "desc"))
    return items


@app.delete("/items/{item_id}")
def remove_item(item_id: int):
    items = JsonHandler.load_data(JSON_PATH)
    size = len(items)
    for i in range(size):
        if items[i]["id"] == item_id:
            old_item = items.pop(i)
            JsonHandler.save_data(items, JSON_PATH)
            return old_item


if __name__ == "__main__":
    uvicorn.run(app)
