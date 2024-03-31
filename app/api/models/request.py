from typing import List
from pydantic import BaseModel


class ReqeustData(BaseModel):
    count: int
    rooms: List[int]


class Request(BaseModel):
    data: ReqeustData
    date: str


class Resposne(BaseModel):
    message: str
