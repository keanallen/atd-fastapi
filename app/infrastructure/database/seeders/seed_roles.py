from sqlalchemy import delete

from app.infrastructure.database.models.role_model import RoleModel
from app.core.session import AsyncSessionLocal


async def seed_roles() -> None:
    # Define the roles to be seeded
    roles = [
        {"name": "super_admin", "description": "Attendy - Super Admin with all permissions"},
        {"name": "admin", "description": "Account owner (pays subscription) - - Can manage users and forms."},
        {"name": "staff", "description": "Internal team - Can manage forms and view responses."},
        {"name": "guest", "description": "Can view forms and submit responses"},
    ]

    async with AsyncSessionLocal() as session:
        # delete existing roles to avoid duplicates
        await session.execute(delete(RoleModel))
        for role_data in roles:
            new_role = RoleModel(**role_data)
            session.add(new_role)
        await session.commit()