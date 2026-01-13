from datetime import datetime
from pydantic import BaseModel
from .profiles_shcemas import Profile

class CommentCreate(BaseModel):
    body: str

class CommentCreateRequest(BaseModel):
    comment: CommentCreate

class CommentOut(BaseModel):
    id: str
    body: str
    author: Profile
    createdAt: datetime
    updatedAt: datetime

class CommentResponse(BaseModel):
    comment: CommentOut