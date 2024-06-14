from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    google_sub: str
    name: str
    email: str
    phone: Optional[str] = None
    img_url: Optional[str] = None