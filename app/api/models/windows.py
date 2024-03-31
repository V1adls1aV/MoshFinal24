from pydantic import BaseModel
from .windows_floor import WindowsFloor


class Windows(BaseModel):
    data: WindowsFloor
    description: str
