from fastapi import APIRouter
from typing import Optional


router = APIRouter(
  prefix="/items",
  tags=["items"],
  responses={404: {"description": "Not found"}},
)

fake_items_db = [
  {"item_name": "Foo"},
  {"item_name": "Bar"},
  {"item_name": "Baz"},
  {"item_name": "Plumbus"},
]

@router.get("/")
async def read_items(
  skip: Optional[int] = 0,
  limit: Optional[int] = 10
):
  return fake_items_db[skip : skip + limit]

@router.get("/{item_id}")
async def read_item(item_id: int):
  return {
    "message": "Here is your item:",
    "item_id": item_id,
    "item": fake_items_db[item_id - 1]
  }