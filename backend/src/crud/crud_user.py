from src.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from typing import Optional
import logging

async def create_user(db: AsyncSession, user_data: User) -> User:
    # safety checks
    if "password" in user_data:
        user_data.pop("password")  # never store plain password
    if "hashed_password" not in user_data or not user_data["hashed_password"]:
        raise ValueError("hashed_password is required")

    user = User(**user_data)
    db.add(user)

    try:
        # detect integrity/type errors before full commit
        await db.flush()
        await db.commit()
        await db.refresh(user)
        return user

    except IntegrityError as e:
        await db.rollback()
        logging.exception("IntegrityError while creating user")
        # e.orig has the MySQL error (duplicate, null, etc.)
        raise ValueError(f"Email '{user_data.get('email')}' already exists") from e

    except SQLAlchemyError as e:
        await db.rollback()
        logging.exception("SQLAlchemyError while creating user")
        # bubble up with detail so the caller can 500
        raise RuntimeError(str(e)) from e
    

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result  = await db.execute(select(User).where(User.email == email))
    return result.scalars().first() # scalars() to get ORM objects, first() to get single object or None
