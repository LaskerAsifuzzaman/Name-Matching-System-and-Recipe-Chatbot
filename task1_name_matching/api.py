from fastapi import APIRouter
from pydantic import BaseModel
from .matcher import find_similar_names

router = APIRouter()

class NameRequest(BaseModel):
    name: str

@router.post("/name-match")
def name_match(req: NameRequest):
    return find_similar_names(req.name)
