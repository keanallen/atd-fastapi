from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.session import get_db

from app.application.use_cases.auth_usecase import LoginUseCase
from app.domain.schemas.user_schema import LoginRequest, LoginResponse
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl


router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login_user(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    try:
        if not data.email or not data.password:
            raise HTTPException(status_code=400, detail="Email and password are required")
        user_repository = UserRepositoryImpl(db)
        login_usecase = LoginUseCase(user_repository)
        token = await login_usecase.execute(data.email, data.password)
        if not token:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return LoginResponse(access_token=token, token_type="bearer")
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e))
    