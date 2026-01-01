from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.deps import require_user
from app.schemas.articles_schemas import ArticleRequest, ArticleResponse, UpdateRequest, ArticlesList
from app.service.article_service import create_article_service, update_article_service, delete_article_service
from app.presenters.article_presenter import to_article_detail
from app.repositories.article_repo import get_article_by_slug

router = APIRouter()

@router.post("/articles", response_model=ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article(
    payload: ArticleRequest,
    db: Session = Depends(get_db),
    current=Depends(require_user),
):
    me, _token = current
    a = payload.article
    article = create_article_service(db, me.id, a.title, a.description, a.body, a.tags)
    return to_article_detail(article, following=False)

@router.put("/articles/{slug}" ,response_model=ArticleResponse, status_code=status.HTTP_200_OK)
def update_article(
        slug: str,
        payload: UpdateRequest,
        db: Session = Depends(get_db),
        current = Depends(require_user)
):
    user, token = current
    patch = payload.article
    return to_article_detail(update_article_service(db, user.id, slug, patch))

@router.get("/articles/{slug}", response_model=ArticleResponse, status_code=status.HTTP_200_OK)
def get_an_article(
        slug: str,
        db: Session = Depends(get_db)
):
    article = get_article_by_slug(db, slug)
    if not article:
        raise HTTPException(status_code=422, detail="no such article")

    return to_article_detail(article)

@router.delete("/articles/{slug}", status_code=status.HTTP_200_OK)
def delete_article(
        slug: str,
        db: Session = Depends(get_db),
        current = Depends(require_user)
):
    user, token = current
    user_id = user.id

    delete_article_service(db, slug, user_id)