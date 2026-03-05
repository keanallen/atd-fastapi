from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.database.models.user_model import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        super().__init__()
        self.session = session
    
    async def get_by_email(self, email: str) -> User | None:
        query = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(query)
        user_model = result.scalars().first()
        if user_model:
            return User(
                id=user_model.id,
                first_name=user_model.first_name,
                last_name=user_model.last_name,
                email=user_model.email,
                status=user_model.status,
                hashed_password=user_model.hashed_password
            )
        return None
