from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Track(Base):
    """
    Model that represents a Song

    ...

    Attributes
    ----------
    TrackId : Column(Integer)
        Primary Key
    Name : Column(String)
        Name of the song
    AlbumId : Column(Integer)
        Album ID
    Composer : Column(String)
        Songwriter
    Milliseconds : Column(Integer)
        Duration of the song
    Bytes : Column(Integer)
        Size of the song file
    UnitPrice : Column(DECIMAL)
        Price of the song

    Methods
    -------
    """
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(DECIMAL)
