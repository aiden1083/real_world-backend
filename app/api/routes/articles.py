from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.deps import require_user   # 你 require_user 放哪里就按实际 import 改
from app.schemas.articles_schemas import ArticleRequest, ArticleResponse
from app.service.article_service import create_article
from app.presenters.article_presenter import to_article_detail

router = APIRouter()

@router.post("/articles", response_model=ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article_endpoint(
    payload: ArticleRequest,
    db: Session = Depends(get_db),
    current=Depends(require_user),
):
    me, _token = current
    a = payload.article
    article = create_article(db, me.id, a.title, a.description, a.body, a.tagList)
    return to_article_detail(article, following=False)
