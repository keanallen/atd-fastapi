import asyncio

from app.core.session import engine
from app.infrastructure.database.seeders.seed_users import seed_users
from app.infrastructure.database.seeders.seed_roles import seed_roles
from app.infrastructure.database.seeders.seed_user_roles import seed_user_roles

async def main():
    await seed_roles()
    await seed_users()
    await seed_user_roles()

    # Dispose the engine to close all connections
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())