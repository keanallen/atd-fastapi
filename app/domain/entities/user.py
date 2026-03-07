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
    status: str = "active"
    hashed_password: str = ""
    roles: list[str] = None

    def verify_password(self, password: str) -> bool:
        return verify_password(password, self.hashed_password)

    def has_role(self, role: str) -> bool:
        return role in self.roles if self.roles else False