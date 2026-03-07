from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from app.core.database import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from app.core.config import settings
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

security = HTTPBearer()

def unauthorized_exception(message: str = "Unauthorized") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message,
        headers={"WWW-Authenticate": "Bearer"},
    )

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: AsyncSession = Depends(get_db)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise unauthorized_exception("Could not validate credentials")
        user_repository = UserRepositoryImpl(db)
        user = await user_repository.get_by_email(email)
        if user is None:
            raise unauthorized_exception(f"User with email {email} not found")
        return user
    except jwt.ExpiredSignatureError:
        raise unauthorized_exception("Token has expired")
    except jwt.JWTError:
        raise unauthorized_exception("Could not validate credentials")
