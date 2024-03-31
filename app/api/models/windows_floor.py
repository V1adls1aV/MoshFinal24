from typing import List
from pydantic import BaseModel


class WindowsFloor(BaseModel):
    floor_1: List[bool]
    floor_2: List[bool]
    floor_3: List[bool]
    floor_4: List[bool]
    floor_5: List[bool]
    floor_6: List[bool]
    floor_7: List[bool]
    floor_8: List[bool]
