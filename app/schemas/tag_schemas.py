from pydantic import BaseModel

class Tags(BaseModel):
    tags: list[str]