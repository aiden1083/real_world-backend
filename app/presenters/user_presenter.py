from app.schemas.user_schemas import UserDetail, UserResponse

def to_user_detail(user, token: str) -> UserResponse:
    return UserResponse(
        user=UserDetail(
            bio=user.bio,
            email=user.email,
            username=user.username,
            image=user.image,
            token=token
        )
    )