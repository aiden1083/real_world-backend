from pydantic import BaseModel
from datetime import datetime
from .profiles_shcemas import Profile


class ArticleOutput(BaseModel):
    slug: str
    title: str
    description: str
    body: str
    tags: list[str]
    createdAt: datetime
    updateAt: datetime
    favorited: bool
    favoritesCount: int
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

class UpdateArticle(BaseModel):
    title: str
    description: str
    body: str

class UpdateRequest(BaseModel):
    article: UpdateArticle

class ArticlesList(BaseModel):
    articles: list[ArticleOutput]
    articlesCount: int

