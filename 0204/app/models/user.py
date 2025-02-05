from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    login_id: str
    password: str
    name: Optional[str] = None

    def validate(self) -> bool:
        if self.login_id == "" or self.password == "":
            return False
        if self.password.find("'") != -1 or self.password.find('"') != -1:
            return False
        return True