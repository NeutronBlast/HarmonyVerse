from config.db import SessionLocal
from models.album import Album
from models.track import Track


def get_songs_album(album_id):
    """Returns all the tracks from an album

    Parameters
    ----------
    album_id : int
        Album ID

    Returns
    ------
    list
        List of songs that belong to an album
    """
    db = SessionLocal()
    songs = db.query(Track).filter(Track.AlbumId == album_id).all()
    db.close()
    return songs
