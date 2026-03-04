from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.core.session import AsyncSessionLocal
from app.core.utils import hash_password
from app.infrastructure.database.models.user_model import UserModel


async def seed_users() -> None:
	super_admin = {
			"first_name": "Super",
			"last_name": "Admin",
			"email": "sa@attendy.io",
			"hashed_password": hash_password("password123"),
			"status": "active",
			}

	async with AsyncSessionLocal() as session:
		new_user = UserModel(**super_admin)
		session.add(new_user)
		try:
			await session.commit()
		except IntegrityError:
			await session.rollback()
			raise