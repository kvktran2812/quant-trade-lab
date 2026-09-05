"""
FastAPI starter application.

Run with:
    uvicorn main:app --reload

Docs available at:
    http://127.0.0.1:8000/docs
"""

from datetime import datetime
from typing import Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Sample API",
    description="A simple starter FastAPI application with CRUD endpoints.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, examples=["Widget"])
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0, examples=[9.99])
    in_stock: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    in_stock: Optional[bool] = None


class Item(ItemBase):
    id: str
    created_at: datetime
    updated_at: datetime


# ---------------------------------------------------------------------------
# In-memory "database"
# ---------------------------------------------------------------------------

db: dict[str, Item] = {}

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.get("/", tags=["Health"])
def read_root():
    return {"status": "ok", "message": "Welcome to the Sample API"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


@app.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["Items"],
)
def create_item(item: ItemCreate):
    now = datetime.utcnow()
    new_item = Item(
        id=str(uuid4()),
        created_at=now,
        updated_at=now,
        **item.model_dump(),
    )
    db[new_item.id] = new_item
    return new_item


@app.get("/items", response_model=list[Item], tags=["Items"])
def list_items(
    in_stock: Optional[bool] = Query(None, description="Filter by stock status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
):
    items = list(db.values())
    if in_stock is not None:
        items = [i for i in items if i.in_stock == in_stock]
    return items[skip : skip + limit]


@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: str):
    item = db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
def update_item(item_id: str, update: ItemUpdate):
    item = db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    update_data = update.model_dump(exclude_unset=True)
    updated_item = item.model_copy(update={**update_data, "updated_at": datetime.utcnow()})
    db[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return None


# ---------------------------------------------------------------------------
# Entrypoint (optional, for `python main.py`)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)