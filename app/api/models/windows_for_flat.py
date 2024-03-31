from typing import List
from pydantic import BaseModel

class WindowsForFlat(BaseModel):
    data: List[int]
    description: str
