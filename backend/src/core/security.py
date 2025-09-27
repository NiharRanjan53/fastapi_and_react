from jose import jwt
from typing import Dict, Any, Optional
from passlib.context import CryptContext
import datetime
from src.core.config import settings


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
ALGORITHM = "HS256"

def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: Dict[str, Any], expires_minutes: Optional[int] = None) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire, "iat": datetime.datetime.now(datetime.timezone.utc)})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)