import decimal
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Track(BaseModel):
    id: int
    name: str
    album_id: int
    composer: str
    milliseconds: int
    bytes: int
    unit_price: decimal
