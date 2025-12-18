from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)

class UserRegisterRequest(BaseModel):
    user: UserRegister

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserLoginRequest(BaseModel):
    user: UserLogin

class UserDetail(BaseModel):
    bio: str | None = ""
    email: EmailStr
    image: str | None = ""
    token: str
    username:str

class UserResponse(BaseModel):
    user:UserDetail

class UpdateCurrentUserRequest(BaseModel):
    bio: str
    email: EmailStr
    image: str
    username: str








