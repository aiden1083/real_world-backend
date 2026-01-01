from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.article_model import Article

def get_article_by_slug(db: Session, slug: str) -> Article | None:
    return db.scalar(select(Article).where(Article.slug == slug))

