from pydantic import BaseModel

class Data(BaseModel):
  user_id: int
  email: str
  address: str
  phone: str