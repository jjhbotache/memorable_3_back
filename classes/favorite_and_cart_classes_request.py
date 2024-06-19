from pydantic import BaseModel

class CrudFavoriteAndCartDesignRequest(BaseModel):
    user_sub: str
    design_id: int
