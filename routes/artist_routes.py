from fastapi import APIRouter

from repositories.artist_repository import get_all_artists, get_albums_artist, get_songs_artist

router = APIRouter()


@router.get("/music-store/api/v1/singers")
async def get_artists():
    """Returns all the artists stored in the DB

    Parameters
    ----------

    Returns
    ------
    list
        List of artists
    """
    artists = get_all_artists()
    return {"artists": artists}


@router.get("/music-store/api/v1/singers/{id}")
async def get_singer_albums(id):
    """Returns all the albums by artist

    Parameters
    ----------
    id : int
        Artist ID

    Returns
    ------
    list
        List of albums made by an artist
    """
    albums = get_albums_artist(id)
    return {"albums": albums}


@router.get("/music-store/api/v1/singer/{id}")
async def get_tracks_artist(id):
    """Returns all the tracks by artist

    Parameters
    ----------
    id : int
        Artist ID

    Returns
    ------
    list
        List of tracks made by an artist
    """
    songs = get_songs_artist(id)
    return {"songs": songs}
