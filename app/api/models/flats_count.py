from pydantic import BaseModel

class FlatsCount(BaseModel):
    data: int
    description: str