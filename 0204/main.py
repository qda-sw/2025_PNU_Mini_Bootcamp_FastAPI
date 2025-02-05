from fastapi import *
from app.routers import auth
from app.routers import posts

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)

