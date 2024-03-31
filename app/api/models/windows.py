from pydantic import BaseModel
from typing import List


class Windows(BaseModel):
    data: List[List[bool]]
    description: str
