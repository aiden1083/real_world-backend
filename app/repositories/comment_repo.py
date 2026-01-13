from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.models.comment_model import Comment

def create_comment(db: Session, body: str, article_id: int, author_id: int) -> Comment:
    comment = Comment(body=body,
                      article_id=article_id,
                      author_id=author_id,
                      created_at=datetime.now(timezone.utc),
                      updated_at=datetime.now(timezone.utc)
                      )
    db.add(comment)
    db.flush()
    db.refresh(comment)
    return comment

