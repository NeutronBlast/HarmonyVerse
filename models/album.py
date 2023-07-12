from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Album(Base):
    """
    Model that represents an Album

    ...

    Attributes
    ----------
    AlbumId : Column(Integer)
        Primary Key
    Title : Column(String)
        Name of the album
    ArtistId : Column(Integer)
        Artist ID

    Methods
    -------
    """
    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer)
