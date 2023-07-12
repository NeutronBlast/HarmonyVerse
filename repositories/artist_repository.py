from config.db import SessionLocal
from models.album import Album
from models.artist import Artist
from models.track import Track


def get_all_artists():
    """Returns all the artists stored in the DB

    Parameters
    ----------

    Returns
    ------
    list
        List of artists
    """
    db = SessionLocal()
    artists = db.query(Artist).all()
    db.close()
    return artists


def get_albums_artist(artist_id):
    """Returns all the albums by artist

    Parameters
    ----------
    artist_id : int
        Artist ID

    Returns
    ------
    list
        List of albums made by an artist
    """
    db = SessionLocal()
    albums = db.query(Album).filter(Album.ArtistId == artist_id).all()
    db.close()
    return albums


def get_songs_artist(artist_id):
    """Returns all the tracks by artist

    Parameters
    ----------
    artist_id : int
        Artist ID

    Returns
    ------
    list
        List of tracks made by an artist
    """
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
