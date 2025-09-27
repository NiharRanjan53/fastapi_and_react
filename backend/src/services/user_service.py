from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from src.crud import crud_user
from src.core.security import get_hashed_password
from src.schemas.auth import UserData

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
