from pydantic import BaseModel

class Date(BaseModel):
    data: int
    description: str