from app.domain.repositories.user_repository import UserRepository
from app.core.utils import create_access_token


class LoginUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str, password: str) -> str:
        user = await self.user_repository.get_by_email(email)
        if not user or not user.verify_password(password):
            raise ValueError("Invalid email or password")
        token = create_access_token({"sub": user.email})
        return token