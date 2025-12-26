from pydantic import BaseModel

class Profile(BaseModel):
    bio: str | None = ""
    image: str | None = ""
    username: str
    following: bool = False

class ProfileResponse(BaseModel):
    profile: Profile