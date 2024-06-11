from pydantic import BaseModel

class SendEmailClass(BaseModel):
  recipent: str
  from_email: str
  from_name: str
  subject: str
  message: str
  
  