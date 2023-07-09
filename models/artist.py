from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
