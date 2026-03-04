from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.core.config import settings

engine = create_async_engine(
    settings.async_database_url,
    echo=True,
    pool_pre_ping=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()

# Import all models to ensure they are registered with SQLAlchemy's metadata
from app.infrastructure.database.models import user_model
from app.infrastructure.database.models import role_model
from app.infrastructure.database.models import user_has_role_model