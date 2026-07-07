
from pydantic import BaseModel


class PostCreate(BaseModel):

    content: str


class PostResponse(BaseModel):

    id: int
    content: str
    user_id: int
    username: str

    class Config:

        from_attributes = True
