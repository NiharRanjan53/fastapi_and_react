from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from src.crud import crud_user
from src.core.security import get_hashed_password, verify_password, create_access_token
from src.schemas.auth import UserData, LoginInfo

async def register_user(db: AsyncSession, user_data: UserData):
    existing = await crud_user.get_user_by_email(db, user_data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    data = user_data.model_dump()
    data["hashed_password"] = get_hashed_password(data.pop("password"))

    try:
        user = await crud_user.create_user(db, data)
        return user
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error while creating user"
        )
    
async def login_user(db: AsyncSession, login_info: LoginInfo):
    user = await crud_user.get_user_by_email(db, login_info.email)
    if not user or not verify_password(login_info.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    if hasattr(user, "is_active") and not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    token = create_access_token({"sub": user.email})
    return token
