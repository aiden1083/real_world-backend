from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.profiles_shcemas import ProfileResponse
from app.repositories.user_repo import get_by_username
from app.api.deps import get_db, require_user


router = APIRouter()

@router.get("/profiles/{username}", response_model=ProfileResponse)
def get_a_profile(username: str, db: Session = Depends(get_db)):
    user = get_by_username(db, username)

    if not user:
        raise HTTPException(status_code=422, detail={"errors": {"username": ["is invalid"]}})

    return {
        "profile": {
            "bio": user.bio,
            "image": user.image,
            "username": user.username,
            "following": False

        }
    }

@router.put("/profiles/{username}/follow", response_model=ProfileResponse)
def follow_user(username: str, db: Session = Depends(get_db), current=Depends(require_user)):
    return