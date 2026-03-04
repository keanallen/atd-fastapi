from sqlalchemy import Column, DateTime, Integer, String, func, Enum
from app.core.database import Base


class RoleModel(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum("super_admin", "admin", "staff","guest", name="role_name"), default="guest", nullable=False)
    description = Column(String(length=255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())