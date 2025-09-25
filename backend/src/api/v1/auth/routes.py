from fastapi import APIRouter

router = APIRouter()
@router.get("/auth")
async def landing_page():
    return {"message": "Welcome to the v1 Auth API"}
