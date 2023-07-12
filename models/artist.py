from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    """
    Model that represents an Artist

    ...

    Attributes
    ----------
    ArtistId : Column(Integer)
        Primary Key
    Name : Column(String)
        Name of the artist

    Methods
    -------
    """
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
