from fastapi import APIRouter

from app.routers import users, posts

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(posts.router, prefix="/posts", tags=["Posts"])
