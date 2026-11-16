from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Sample App")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ItemUpdate(BaseModel):
    name: str
    description: Optional[str] = None


items: list[Item] = []
next_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items", response_model=list[Item])
def list_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    item = Item(id=next_id, name=payload.name, description=payload.description)
    items.append(item)
    next_id += 1
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated = Item(id=item_id, name=payload.name, description=payload.description)
            items[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return
    raise HTTPException(status_code=404, detail="Item not found")
