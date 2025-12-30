from app.schemas.profiles_shcemas import ProfileResponse, Profile

def to_profile_detail(user, following: bool):
    return ProfileResponse(
        profile=Profile(
            bio=user.bio,
            image=user.image,
            username=user.username,
            following=following
        )
    )