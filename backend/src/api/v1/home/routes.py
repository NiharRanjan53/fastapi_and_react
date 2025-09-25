from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def landing_page():
    return {"message": "Welcome to the v1 Home API"}