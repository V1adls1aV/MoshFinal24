from pydantic import BaseModel
from .date import Date
from .flats_count import FlatsCount
from .windows import Windows
from .windows_for_flat import WindowsForFlat


class InfoByDate(BaseModel):
    date: Date
    flats_count: FlatsCount
    windows: Windows
    windows_for_flat: WindowsForFlat
