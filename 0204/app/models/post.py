from dataclasses import dataclass
from typing import Optional

@dataclass
class Post:
    title: str
    body: str
    published: bool
    id: Optional[int] = None
    created_at: Optional[int] = None


@dataclass
class PostResponse:
    post: Optional[Post]
    err_msg: Optional[str] = None