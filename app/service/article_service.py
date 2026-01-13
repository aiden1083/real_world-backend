from __future__ import annotations
from typing import TYPE_CHECKING
import re
import secrets
from datetime import datetime, timezone
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.article_model import Article
from app.models.tag_model import Tag
from app.schemas.articles_schemas import UpdateArticle
from app.repositories.article_repo import get_article_by_slug

if TYPE_CHECKING:
    from app.models.user_model import User

def _slugify(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "article"

def _unique_slug(db: Session, title: str) -> str:
    base = _slugify(title)
    slug = base
    while db.scalar(select(Article).where(Article.slug == slug)) is not None:
        slug = f"{base}--{secrets.token_hex(3)}"
    return slug

def create_article_service(db: Session,
                           author_id: int,
                           title: str,
                           description: str,
                           body: str,
                           tag_list: list[str]) -> Article:
    slug = _unique_slug(db, title)

    article = Article(
        slug=slug,
        title=title,
        description=description,
        body=body,
        author_id=author_id,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    tags: list[Tag] = []
    for raw in tag_list or []:
        name = raw.strip()
        if not name:
            continue

        tag = db.scalar(select(Tag).where(Tag.name == name))
        if not tag:
            tag = Tag(name=name)
            db.add(tag)
            db.flush()
        tags.append(tag)

    article.tags = tags

    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def update_article_service(db: Session,
                   user_id: int,
                   slug: str,
                   patch: UpdateArticle):
    article = get_article_by_slug(db, slug)

    if not article:
        raise HTTPException(status_code=422, detail="")

    if article.author_id != user_id:
        raise HTTPException(status_code=422, detail="")

    if patch.title is not None:
        article.title = patch.title
        article.slug = _unique_slug(db, patch.title)

    if patch.description is not None:
        article.description = patch.description

    if patch.body is not None:
        article.body = patch.body

    db.commit()
    db.refresh(article)
    return article

def delete_article_service(db: Session, slug: str, user_id: int):
    article1 = get_article_by_slug(db, slug)

    if not article1:
        raise HTTPException(status_code=422, detail="no such an article")

    if article1.author_id != user_id:
        raise HTTPException(status_code=422, detail="user is not author")

    db.delete(article1)
    db.commit()



