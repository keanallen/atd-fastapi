from sqlalchemy import Boolean, Column, DateTime, Integer, String, func

from app.core.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(length=50), nullable=False)
    last_name = Column(String(length=50), nullable=False)
    email = Column(String(length=100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=100), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())