from fastapi import APIRouter
from app.api.routes import user,users,tags

api_router = APIRouter()
api_router.include_router(user.router, tags=["user"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(tags.router, tags=["tag"])