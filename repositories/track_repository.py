from config.db import SessionLocal
from models.track import Track


def get_song(song_id):
    """Returns the details about a specific song

    Parameters
    ----------
    song_id : int
        Song ID

    Returns
    ------
    dict
        Song details
    """
    db = SessionLocal()
    song = db.query(Track).filter(Track.TrackId == song_id).first()
    db.close()
    return song
