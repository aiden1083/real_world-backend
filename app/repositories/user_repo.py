from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user_model import User

'''secondary key look-up'''
def get_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))

'''primary key look-up is easier'''
def get_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)

def get_by_username(db: Session, username: str) -> User | None:
    return db.scalar(select(User).where(User.username == username))

def create_user(db: Session, email: str, username: str, hashed_password: str) -> User:
    user = User(email=email, username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
