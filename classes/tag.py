import pydantic

class Tag(pydantic.BaseModel):
  id_tag: int
  name: str