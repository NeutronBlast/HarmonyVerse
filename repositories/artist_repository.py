from config.db import SessionLocal
from models.album import Album
from models.artist import Artist
from models.track import Track


def get_all_artists():
    db = SessionLocal()
    artists = db.query(Artist).all()
    db.close()
    return artists


def get_albums_artist(artist_id):
    db = SessionLocal()
    albums = db.query(Album).filter(Album.ArtistId == artist_id).all()
    db.close()
    return albums


def get_songs_artist(artist_id):
    db = SessionLocal()
    songs = (
        db.query(Track)
        .join(Album, Album.AlbumId == Track.AlbumId)
        .join(Artist, Artist.ArtistId == Album.ArtistId)
        .filter(Artist.ArtistId == artist_id)
        .all()
    )
    db.close()
    return songs
