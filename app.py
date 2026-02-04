from fastapi import FastAPI
from task1_name_matching.api import router as name_router
from task2_recipe_chatbot.api import router as recipe_router

app = FastAPI(
    title="Bookxpert AIML Assignment",
    version="1.0"
)

app.include_router(name_router, prefix="/api")
app.include_router(recipe_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "Running"}
