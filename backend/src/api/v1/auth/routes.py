from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.auth import UserData, UserResponse, LoginInfo, LoginResponse, TockenResponse
from src.services.user_service import login_user, register_user
from src.db.session import get_db


router = APIRouter()

@router.post("/signup", response_model=UserResponse, status_code=201)
async def signup(user_data: UserData, db: AsyncSession = Depends(get_db)):
    user = await register_user(db, user_data)
    return user

@router.post("/login", response_model=TockenResponse, status_code=200)
async def login(payload: LoginInfo, db: AsyncSession = Depends(get_db)):
    token = await login_user(db, payload)
    return {"access_token": token, "token_type": "bearer"}