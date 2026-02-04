from typing import List, Dict, Any
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "recipes.json"


def load_recipes():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


RECIPES = load_recipes()


def find_recipe_by_ingredients(ingredients: List[str]) -> Dict[str, Any]:
    ingredients_set = set(map(str.lower, ingredients))

    # 1️⃣ Try dataset match
    for item in RECIPES:
        if ingredients_set.issubset(set(item["ingredients"])):
            return item["recipe"]

    # 2️⃣ Try LLM fallback (optional)
    try:
        from .llm import generate_recipe_llm

        return {
            "name": "LLM Suggested Recipe",
            "steps": generate_recipe_llm(ingredients).split("\n")
        }
    except Exception as e:
        # 3️⃣ Safe fallback
        return {
            "name": "No Recipe Found",
            "steps": [
                "No matching recipe in dataset.",
                "LLM is unavailable or not installed."
            ]
        }
