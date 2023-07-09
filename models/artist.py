from pydantic import BaseModel


class Artist(BaseModel):
    __tablename__ = 'artists'

    id: int
    name: str
