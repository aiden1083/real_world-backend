from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.comment_model import Comment
from app.repositories.article_repo import get_article_by_slug
from app.repositories.comment_repo import create_comment

def create_comment_service(db: Session, slug: str, body: str) -> Comment:
    article1 = get_article_by_slug(db, slug)

    if not article1:
        raise HTTPException(status_code=422, detail="no such article")

    comment = create_comment(db, body, article1.id, article1.author_id)

    db.commit()
    db.refresh(comment)
    return comment