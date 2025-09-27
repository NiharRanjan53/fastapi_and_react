from fastapi import Depends
from fastapi.security import HTTPBearer, OAuth2PasswordBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.services.user_service import resolve_user_from_token

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login") # Needs to give username and password in swagger
bearer_scheme = HTTPBearer(auto_error=True)  # Swagger will show a single token box

async def get_current_user(creds: HTTPAuthorizationCredentials  = Depends(bearer_scheme), db: AsyncSession = Depends(get_db)):
    token = creds.credentials  # the raw Bearer token
    return await resolve_user_from_token(token, db)