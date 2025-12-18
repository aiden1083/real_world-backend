from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user_schemas import UserRegisterRequest, UserLoginRequest, UserResponse
from app.service.user_service import register_user, login_user
from app.presenters.user_presenter import to_user_detail

router = APIRouter()

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserRegisterRequest, db: Session = Depends(get_db)):
    u = payload.user
    user, token = register_user(db, str(u.email), u.username, u.password)
    return to_user_detail(user, token)

@router.post("/users/login", response_model=UserResponse)
def login(payload: UserLoginRequest, db: Session = Depends(get_db)):
    u = payload.user
    user, token = login_user(db, str(u.email), u.password)
    return to_user_detail(user, token)