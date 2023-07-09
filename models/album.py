from pydantic import BaseModel


class Album(BaseModel):
    __tablename__ = 'albums'

    id: int
    title: str
    artist_id: int