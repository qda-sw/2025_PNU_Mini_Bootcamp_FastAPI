from fastapi import APIRouter
from app.models.auth import *
from app.models.user import *
router = APIRouter(
    prefix="/auth",
)


@router.post("/signup", status_code=201)
def signup(user: User) -> AuthResponse:
    if not user.validate():
        return AuthResponse(jwt_token=None, err_msg="Invalid user")
    return AuthResponse(jwt_token="wow", err_msg="Not implemented")

@router.post("/authsignin", status_code=200)
def signin(user: User) -> AuthResponse:
    return AuthResponse(jwt_token=None, err_msg="Not implemented")