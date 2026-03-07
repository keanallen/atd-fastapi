from sqlalchemy import insert, select

from app.core.session import AsyncSessionLocal
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.database.models.user_has_role_model import UserHasRoleModel
from app.infrastructure.database.models.user_model import UserModel


async def seed_user_roles() -> None:
    async with AsyncSessionLocal() as session:
        # check for role id based on name "super_admin"
        sa_query = select(UserModel).where(UserModel.email == "sa@attendy.io")
        super_admin = await session.execute(sa_query)
        super_admin = super_admin.scalars().first()
        if super_admin:
            # assign super_admin role to the user
            role_query = select(RoleModel).where(RoleModel.name == "super_admin")
            super_admin_role = await session.execute(role_query)
            super_admin_role = super_admin_role.scalars().first()
            if super_admin_role:
                # insert into user_has_role table
                query = insert(UserHasRoleModel).values(user_id=super_admin.id, role_id=super_admin_role.id)
                await session.execute(query)
                await session.commit()
