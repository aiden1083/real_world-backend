from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password, create_access_token
from app.repositories import user_repo

def register_user(db: Session, email: str, username: str, password: str):
    if user_repo.get_by_email(db, email):
        raise HTTPException(status_code=422, detail={"errors": {"email": ["has already been taken"]}})

    user = user_repo.create_user(db, email, username, hash_password(password))
    token = create_access_token(subject=str(user.id))
    return user, token

def login_user(db: Session, email: str, password: str):
    user = user_repo.get_by_email(db, email)
    if not user or not verify_password(password, str(user.hashed_password)):
        raise HTTPException(status_code=422, detail={"errors": {"email or password": ["is invalid"]}})

    token = create_access_token(subject=str(user.id))

    return user, token