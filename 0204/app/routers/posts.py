from fastapi import APIRouter
from app.models.post import *
import time
router = APIRouter(
    prefix="/posts",
)

@router.get("/", status_code=200)
def get_posts(page:int = 1, limit:int = 10) -> PostResponse:
    return PostResponse(post=[
        Post(id=1, title="Title", body="Body", created_at=int(time.time()), published=True)
    ], err_msg="Not implemented")

@router.get("/{post_id}", status_code=200)
def get_post(post_id: int) -> PostResponse:
    return PostResponse(post=[
        Post(id=1, title="Title", body="Body", created_at=int(time.time()), published=True)
    ], err_msg="Not implemented")

@router.post("/", status_code=201)
def create_post(post: Post) -> PostResponse:
    return PostResponse(post=[
        Post(id=1, title="Title", body="Body", created_at=int(time.time()), published=True)
    ], err_msg="Not implemented")

@router.put("/{post_id}", status_code=200)
def update_post(post: Post, post_id: int) -> PostResponse:
    return PostResponse(post=[
        Post(id=1, title="Title", body="Body", created_at=int(time.time()), published=True)
    ], err_msg="Not implemented")

@router.put("/{post_id}/publish", status_code=200)
def publish_post(post_id: int|None = None, publish: bool = False) -> PostResponse:
    return PostResponse(post=[
        Post(id=1, title="Title", body="Body", created_at=int(time.time()), published=True)
    ], err_msg="Not implemented")

@router.delete("/{post_id}", status_code=200)
def delete_post(post_id: int) -> PostResponse:
    return PostResponse(post=None, err_msg="Not implemented")