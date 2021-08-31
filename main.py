from fastapi import FastAPI

from routers import items, models

app = FastAPI()

# ADD ROUTERS BEFORE
app.include_router(items.router)
app.include_router(models.router)


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
