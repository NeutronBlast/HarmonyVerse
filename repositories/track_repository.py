from config.db import SessionLocal
from models.track import Track


def get_song(song_id):
    db = SessionLocal()
    albums = db.query(Track).filter(Track.TrackId == song_id).first()
    db.close()
    return albums
