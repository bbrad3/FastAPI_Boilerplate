from enum import Enum
from typing import Optional
from fastapi import FastAPI
app = FastAPI()

class ModelName(str, Enum):
  mod1 = "mod1"
  mod2 = "mod2"
  mod3 = "mod3"

@app.get("/")
async def root():
    return {"message": "FastAPI root route!"}

@app.post("/create")
async def create():
  return {"message": "Create route!"}

@app.put("/update")
async def update():
  return {"message": "Update route!"}

@app.delete("/delete")
async def destroy():
  return {"message": "Destroy route!"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items")
async def read_items(skip: Optional[int] = 0, limit: Optional[int] = 10):
  return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {
    "message": "Here is your item:",
    "item_id": item_id,
    "item": fake_items_db[item_id - 1]
  }

@app.get("/models/{model_name}")
async def read_model(model_name: ModelName):
  if model_name == ModelName.mod1:
    return {"model": model_name, "message": "Good choice!"}
  if model_name == ModelName.mod2:
    return {"model": model_name, "message": "Not bad!"}
  if model_name.value == "mod3":
    return {"model": model_name, "message": "You get the scraps!"}
  return {"message": "I don't know that model!"}


