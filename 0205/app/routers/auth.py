from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models.auth import *
from app.models.user import *
from app.dependencies.db import get_db_session
import random
router = APIRouter(
    prefix="/auth",
)


@router.post("/signup", status_code=201)
def signup(user: User = Depends(validate_user),
           session: Session = Depends(get_db_session)) -> AuthResponse:
    if session.get(User, user.login_id):
        return AuthResponse(jwt_token=None, err_msg="User already exists")
    session.add(user)
    session.commit()
    session.refresh(user)
    return AuthResponse(jwt_token=random.randint(1, 10**6), err_msg=None)

@router.post("/signin", status_code=200)
def signin(user: User = Depends(validate_user),
           session: Session = Depends(get_db_session)) -> AuthResponse:
    on_db_user = session.get(User, user.login_id)
    if not on_db_user or on_db_user.password != user.password:
        return AuthResponse(jwt_token=None, err_msg="User not found or Invalid password")
    return AuthResponse(jwt_token=random.randint(1, 10**6), err_msg=None)