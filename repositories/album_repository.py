from config.db import SessionLocal
from models.album import Album
from models.track import Track


def get_songs_album(album_id):
    db = SessionLocal()
    songs = db.query(Track).filter(Track.AlbumId == album_id).all()
    db.close()
    return songs
