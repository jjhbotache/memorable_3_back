from pydantic import BaseModel
from .user import User

class CreateData(BaseModel):
  user_id: int
  password: str
  email: str
  address: str
  phone: str