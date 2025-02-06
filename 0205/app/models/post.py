from fastapi import HTTPException, status
from sqlmodel import SQLModel, Field
from dataclasses import dataclass
from typing import Optional

class Post(SQLModel, table=True):
    title: str
    body: str
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[int] = Field(default= None, index=True)
    published: bool = Field(index=True)

def validate_post(post: Post) -> Post:
    if post.title == "" or post.body == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title or Body cannot be empty"
        )
    return post

@dataclass
class PostResponse:
    posts: list[Optional[Post]]
    err_msg: Optional[str] = None