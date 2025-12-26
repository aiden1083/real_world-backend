from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password, create_access_token
from app.repositories import user_repo
from app.schemas.user_schemas import UpdateCurrentUserRequest

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

def update_user(db: Session, user, data: UpdateCurrentUserRequest):
    if data is None:
        raise HTTPException(status_code=422, detail={"errors": {"input": ["at least one field is required"]}})

    if data.email is not None:
        if data.email != user.email:
            other = user_repo.get_by_email(db, str(data.email))
            if other and other.id != user.id:
                raise HTTPException(status_code=422, detail={"errors": {"email": ["has already been taken"]}})
            user.email = data.email

    if data.username is not None:
        if data.username != user.username:
            other = user_repo.get_by_username(db, str(data.username))
            if other and other.id != user.id:
                raise HTTPException(status_code=422, detail={"errors": {"username": ["has already been taken"]}})
            user.email = data.email

    if data.bio is not None:
        user.bio = data.bio

    if data.image is not None:
        user.image = data.iamge

    db.commit()
    db.refresh(user)
    return user