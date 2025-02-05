from dataclasses import dataclass
from typing import Optional

@dataclass
class AuthResponse:
    jwt_token: Optional[str] = None
    err_msg: Optional[str] = None