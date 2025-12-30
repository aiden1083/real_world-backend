def to_article_detail(article, following: bool = False):
    return {
        "article": {
            "slug": article.slug,
            "title": article.title,
            "description": article.description,
            "body": article.body,
            "tags": [t.name for t in article.tags or []],
            "createAt": article.created_at,
            "updateAt": article.updated_at,
            "favorited": False,
            "favoriteCount": 0,
            "author": {
                "bio": article.author.bio,
                "image": article.author.image or "",
                "username": article.author.username or "",
                "following": following
            }
        }
    }