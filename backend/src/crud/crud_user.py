from src.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from typing import Optional

async def create_user(db: AsyncSession, user_data: User) -> User:
    user = User(**user_data)
    db.add(user)
    try:
        await db.commit()
        await db.refresh(user)
        return user
    except IntegrityError as e:
        await db.rollback()
        # This happens e.g. if username/email is duplicate
        raise ValueError(f"User with email '{user.email}' already exists") from e
    except SQLAlchemyError as e:
        await db.rollback()
        # Generic SQLAlchemy error
        raise RuntimeError("Database error while creating user") from e
    

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result  = await db.execute(select(User).where(User.email == email))
    return result.scalars().first() # scalars() to get ORM objects, first() to get single object or None
