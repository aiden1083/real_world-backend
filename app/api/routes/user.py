from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.service.user_service import update_user
from app.schemas.user_schemas import UserResponse, UpdateCurrentUserRequest
from app.api.deps import require_user, get_db
from app.presenters.user_presenter import to_user_detail

router = APIRouter()

@router.get("/user", response_model=UserResponse)
def get_current_user(current=Depends(require_user)):
    user, token = current
    return to_user_detail(user, token)

@router.put("/user", response_model=UserResponse)
def update_current_user(payload: UpdateCurrentUserRequest,
                        db: Session = Depends(get_db),
                        current = Depends(require_user)):
    user, token = current
    user = update_user(db, user, payload)

    return to_user_detail(user, token)