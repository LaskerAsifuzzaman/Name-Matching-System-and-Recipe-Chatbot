from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .service import find_recipe_by_ingredients

router = APIRouter()

from typing import List
from pydantic import BaseModel

class RecipeRequest(BaseModel):
    ingredients: List[str]

@router.post("/recipe")
def get_recipe(req: RecipeRequest):
    if not req.ingredients:
        raise HTTPException(status_code=400, detail="Ingredients list cannot be empty")

    recipe = find_recipe_by_ingredients(req.ingredients)

    return {
        "ingredients": req.ingredients,
        "recipe": recipe
    }
