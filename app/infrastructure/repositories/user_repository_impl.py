from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.database.models.user_has_role_model import UserHasRoleModel
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
            roles_query = (
                select(RoleModel.name)
                .join(UserHasRoleModel, UserHasRoleModel.role_id == RoleModel.id)
                .where(UserHasRoleModel.user_id == user_model.id)
            )
            roles_result = await self.session.execute(roles_query)
            role_names = [role_name for role_name in roles_result.scalars().all()]

            return User(
                id=user_model.id,
                first_name=user_model.first_name,
                last_name=user_model.last_name,
                email=user_model.email,
                status=user_model.status,
                hashed_password=user_model.hashed_password,
                roles=role_names,
            )
        return None
