from fastapi import Depends, APIRouter, HTTPException, status
from sqlmodel import Session, select, update
from app.models.post import *
from app.dependencies.db import get_db_session
import time
router = APIRouter(
    prefix="/posts",
)

@router.get("/", status_code=200)
def get_posts(page:int = 1, 
              limit:int = 10,
              session:Session = Depends(get_db_session)) -> PostResponse:
    if page < 1:
        page = 1
    if limit < 1 or limit > 10:
        limit = 10
    nOffset = (page - 1) * limit
    posts = session.exec(
        select(Post).offset(nOffset).limit(limit)
    ).all()
    return PostResponse(posts=posts, err_msg=None)

@router.get("/{post_id}", status_code=200)
def get_post(post_id: int,
             session: Session = Depends(get_db_session)) -> PostResponse:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostResponse(posts=[post], err_msg=None)

@router.post("/", status_code=201)
def create_post(post: Post = Depends(validate_post), 
                session: Session = Depends(get_db_session)) -> PostResponse:
    post.created_at = int(time.time())
    session.add(post)
    session.commit()
    session.refresh(post)
    return PostResponse(posts=[post], err_msg=None)

@router.put("/{post_id}", status_code=200)
def update_post(post_id: int, 
                post: Post = Depends(validate_post), 
                session: Session = Depends(get_db_session)) -> PostResponse:
    old_post = session.get(Post, post_id)
    if not old_post:
        raise HTTPException(status_code=404, detail="Post not found")
    postData = post.model_dump(exclude_unset=True)
    old_post.sqlmodel_update(postData)
    session.add(old_post)
    session.commit()
    session.refresh(old_post)
    return PostResponse(posts=[old_post], err_msg=None)

@router.put("/{post_id}/publish", status_code=200)
def publish_post(post_id: int|None = None, 
                 publish: bool = False,
                 session:Session = Depends(get_db_session)) -> PostResponse:
    if post_id < 1:
        raise HTTPException(status_code=400, detail="Invalid post id")
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.sqlmodel_update({"published": publish})
    session.commit()
    session.refresh(post)
    return PostResponse(posts=[post], err_msg=None)

@router.delete("/{post_id}", status_code=200)
def delete_post(post_id: int,
                session: Session = Depends(get_db_session)) -> PostResponse:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    session.delete(post)
    session.commit()
    return PostResponse(posts=[], err_msg=None)