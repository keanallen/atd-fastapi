from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.session import get_db
from app.core.deps import get_current_user, require_roles

from app.application.use_cases.auth_usecase import LoginUseCase
from app.domain.schemas.user_schema import LoginRequest, LoginResponse
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl


router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login_user(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    """
    Authenticate a user and return a JWT token.
    """
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


@router.get("/me")
async def get_current_user(current_user = Depends(get_current_user)):
    """
    Get the current authenticated user.

    This endpoint returns the details of the currently authenticated user based on the provided JWT token.
    """
    try:
        return current_user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e))


@router.get("/admin-only")
async def admin_only_endpoint(current_user = Depends(require_roles(["super_admin"]))):
    """
    An example endpoint that requires admin role.

    This endpoint is protected by a role guard that checks if the current user has the "admin" role.
    """
    return {"message": "Welcome, admin!"}