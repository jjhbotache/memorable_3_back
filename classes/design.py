import pydantic

class Design(pydantic.BaseModel):
    id_design: int
    name: str
    img_url: str
    ai_url: str
    