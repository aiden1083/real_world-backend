from fastapi_cloud_cli.commands.env import delete
from sqlalchemy.orm import Session
from sqlalchemy import select, exists, func
from sqlalchemy.dialects.postgresql import insert

from app.models.article_model import Article, users_articles

def get_article_by_slug(db: Session, slug: str) -> Article | None:
    return db.scalar(select(Article).where(Article.slug == slug))

def is_favorited(db: Session, user_id: int, article_id: int) -> bool:
    stmt = select(exists()).select_from(users_articles).where(
        users_articles.c.article_id == article_id,
        users_articles.c.user_id == user_id
    )

    return db.scalar(stmt)

def favorites_count(db: Session, article_id: int) -> int:
    stmt = select(func.count()).where(
        users_articles.c.article_id == article_id
    )

    return db.scalar(stmt) or 0

def favorite(db: Session, user_id: int, article_id) -> None:
    stmt = (insert(users_articles).values(user_id=user_id, article_id=article_id))

    db.execute(stmt)
    db.commit()

def unfavorite(db: Session, user_id: int, article_id) -> None:
    stmt = delete(users_articles).where(
        users_articles.c.user_id == user_id,
        users_articles.c.article_id == article_id)

    db.execute(stmt)
    db.commit()