from sqlalchemy.orm import declarative_base


Base = declarative_base()

# Import all models to ensure they are registered with SQLAlchemy's metadata
from app.infrastructure.database.models import user_model
from app.infrastructure.database.models import role_model
from app.infrastructure.database.models import user_has_role_model