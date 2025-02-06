from sqlmodel import Field, SQLModel
from dataclasses import dataclass
from typing import Optional
from fastapi import HTTPException, status

class User(SQLModel, table=True):
    login_id: str = Field(primary_key=True)
    password: str
    name: Optional[str] = None

def validate_user(user: User) -> User:
    if user.login_id == "" or user.password == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login ID or Password cannot be empty"
        )
    if user.password.find("'") != -1 or user.password.find('"') != -1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password cannot contain quotes"
        )
    return user