from fastapi import *
from app.routers import auth
from app.routers import posts
from app.dependencies.db import get_db_session, create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router)
app.include_router(posts.router)