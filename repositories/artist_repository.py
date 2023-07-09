from config.db import SessionLocal
from models.artist import Artist


def get_all_artists():
    db = SessionLocal()
    artists = db.query(Artist).all()
    db.close()
    return artists
