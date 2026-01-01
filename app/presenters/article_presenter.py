from app.schemas.articles_schemas import ArticleResponse, ArticleOutput, Profile, ArticlesList
from app.models.article_model import Article

def to_article_detail(article: Article, following: bool = False) -> ArticleResponse:
    return ArticleResponse(
        article=ArticleOutput(
            slug=article.slug,
            title=article.title,
            description=article.description,
            body=article.body,
            tags=[t.name for t in article.tags],
            createdAt=article.created_at,
            updateAt=article.updated_at,
            favorited=False,
            favoritesCount=0,
            author=Profile(
                bio=article.author.bio,
                image=article.author.image,
                username=article.author.username,
                following=following
            )
        )
    )

def to_articles_list(articles_raw):
    return ArticlesList(
        articles=[to_article_detail(a).article for a in articles_raw],
        articlesCount=len(articles_raw)
    )