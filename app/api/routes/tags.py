from fastapi import APIRouter
from app.schemas.tag_schemas import TagsResponse

router = APIRouter()

@router.get("/tags", response_model=TagsResponse)
def get_tags():
    return {"tags": []}

