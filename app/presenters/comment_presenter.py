from app.schemas.comment_schemas import CommentResponse, CommentOut, Profile

def to_comment_detail(comment, following: bool = False) -> CommentResponse:
    return CommentResponse(
        comment=CommentOut(
            id=comment.id,
            createdAt=comment.created_at,
            updatedAt=comment.updated_at,
            body=comment.body,
            author=Profile(
                username=comment.author.username,
                bio=comment.author.bio or "",
                image=comment.author.image or "",
                following=following
            )
        )
    )