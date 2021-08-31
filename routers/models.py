from fastapi import APIRouter
from enum import Enum

router = APIRouter(
  prefix="/models",
  tags=["models"],
)

class ModelName(str, Enum):
  mod1 = "mod1"
  mod2 = "mod2"
  mod3 = "mod3"

@router.get("/")
async def read_models():
  return ModelName
    

@router.get("/{model_name}")
async def read_model(model_name: ModelName):
  if model_name == ModelName.mod1:
    return {"model": model_name, "message": "Good choice!"}
  if model_name == ModelName.mod2:
    return {"model": model_name, "message": "Not bad!"}
  if model_name.value == "mod3":
    return {"model": model_name, "message": "You get the scraps!"}