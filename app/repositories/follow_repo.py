from sqlalchemy.orm import Session

from app.models.follow_model import Follow

def is_following(db: Session, follower_id: int, followee_id: int) -> bool:
    return db.get(Follow, (follower_id, followee_id)) is not None

def follow(db: Session, follower_id: int, followee_id: int) -> None:
    if follower_id == followee_id:
        return

    if is_following(db, follower_id, followee_id):
        return

    db.add(Follow(follower_id=follower_id, followee_id=followee_id))
    db.commit()

def unfollow(db: Session, follower_id: int, followee_id: int) -> None:
    row = db.get(Follow, (follower_id, followee_id))
    if not row:
        return
    db.delete(row)
    db.commit()