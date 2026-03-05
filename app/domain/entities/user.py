from dataclasses import dataclass
import datetime
from typing import Optional
from app.core.utils import verify_password


@dataclass
class User:
    id: Optional[int] = None
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    hashed_password: str = ""
    status: str = "active"
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None

    def verify_password(self, password: str) -> bool:
        return verify_password(password, self.hashed_password)