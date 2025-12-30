from fastapi import APIRouter
from app.schemas.tag_schemas import Tags

router = APIRouter()

@router.get("/tags", response_model=Tags)
def get_tags():
    return {"tags": []}

