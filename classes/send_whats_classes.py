from typing import Optional
from pydantic import BaseModel


class SendWhatsRequest(BaseModel):
  to_phone: str
  message: str
  
class SendWhatsImgRequest(BaseModel):
  to_phone: str
  img_url: str
  
class ConfirmWhatsRequest(BaseModel):
  to_phone: str
  design_img_url:str
  design_id: int
  buy: bool
  quantity: Optional[int] = None
  wine: Optional[str] = None
  name: Optional[str] = None
  