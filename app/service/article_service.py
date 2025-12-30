import re
import secrets
from datetime import datetime, timezone
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.article_model import Article
from app.models.tag_model import Tag

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

def create_article(db: Session, author_id: int, title: str, description: str, body: str, tag_list: list[str]) -> Article:
    slug = _unique_slug(db, title)

    article = Article(
        slug=slug,
        title=title,
        description=description,
        body=body,
        author_id=author_id,
        create_at=datetime.now(timezone.utc),
        update_at=datetime.now(timezone.utc)
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


