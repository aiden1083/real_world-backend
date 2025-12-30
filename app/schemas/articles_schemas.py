from pydantic import BaseModel
from datetime import datetime

class Profile(BaseModel):
    bio: str
    image: str
    username: str
    following: bool

class ArticleOutput(BaseModel):
    slug: str
    title: str
    description: str
    body: str
    tags: list[str]
    createdAt: datetime
    updateAt: datetime
    favorited: bool
    favoriteCounts: int
    author: Profile

class ArticleResponse(BaseModel):
    article: ArticleOutput

class ArticleInput(BaseModel):
    title: str
    description: str
    body: str
    tags: list[str]

class ArticleRequest(BaseModel):
    article: ArticleInput



