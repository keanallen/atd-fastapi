from sqlalchemy import Column, DateTime, ForeignKey, Integer, func
from app.core.database import Base


class UserHasRoleModel(Base):
    __tablename__ = "user_has_role"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())