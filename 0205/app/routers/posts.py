from fastapi import Depends, APIRouter, HTTPException, status
from sqlmodel import Session, select, update
from app.dependencies.db import get_db_session
from app.models.post import *
from app.services.post_service import PostService
import time
router = APIRouter(
    prefix="/posts",
)

@router.get("/", status_code=200)
def get_posts(page:int = 1, 
              limit:int = 10,
              session:Session = Depends(get_db_session),
              postService: PostService = Depends()) -> PostResponse:
    result = postService.get_posts(session, page, limit)
    return PostResponse(posts=result, err_msg=None)

@router.get("/{post_id}", status_code=200)
def get_post(post_id: int,
             session: Session = Depends(get_db_session),
             postService: PostService = Depends()) -> PostResponse:
    result = postService.get_post(session, post_id)
    return PostResponse(posts=[result], err_msg=None)

@router.post("/", status_code=201)
def create_post(post: Post = Depends(validate_post), 
                session: Session = Depends(get_db_session),
                postService: PostService = Depends()) -> PostResponse:
    result = postService.create_post(session, post)
    return PostResponse(posts=[result], err_msg=None)

@router.put("/{post_id}", status_code=200)
def update_post(post_id: int, 
                post: Post = Depends(validate_post), 
                session: Session = Depends(get_db_session),
                postService: PostService = Depends()) -> PostResponse:
    result = postService.update_post(session, post_id, post)
    return PostResponse(posts=[result], err_msg=None)

@router.delete("/{post_id}", status_code=200)
def delete_post(post_id: int,
                session: Session = Depends(get_db_session),
                postService: PostService = Depends()) -> PostResponse:
    result = postService.delete_post(session, post_id)
    return PostResponse(posts=[], err_msg=None)