from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.post import Post
import time
class PostService:
    def get_post(self, db: Session, post_id: int) -> Post:
        post = db.get(Post, post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post
    
    def get_posts(self, db: Session, page: int = 1, limit: int = 10) -> list[Post]:
        if page < 1:
            page = 1
        if limit < 1 or limit > 10:
            limit = 10
        nOffset = (page - 1) * limit
        posts = db.exec(
            select(Post).offset(nOffset).limit(limit)
        ).all()
        return posts
    
    def create_post(self, db: Session, post: Post) -> Post:
        post.created_at = int(time.time())
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
    
    def update_post(self, db: Session, post_id: int, post: Post) -> Post:
        old_post = db.get(Post, post_id)
        if not old_post:
            raise HTTPException(status_code=404, detail="Post not found")
        postData = post.model_dump(exclude_unset=True)
        old_post.sqlmodel_update(postData)
        db.add(old_post)
        db.commit()
        db.refresh(old_post)
        return old_post

    def delete_post(self, db: Session, post_id: int) -> None:
        post = db.get(Post, post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        db.delete(post)
        db.commit()