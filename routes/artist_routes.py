from fastapi import APIRouter

from repositories.artist_repository import get_all_artists, get_albums_artist, get_songs_artist

router = APIRouter()


@router.get("/music-store/api/v1/singers")
async def get_artists():
    artists = get_all_artists()
    return {"artists": artists}


@router.get("/music-store/api/v1/singers/{id}")
async def get_singer_albums(id):
    albums = get_albums_artist(id)
    return {"albums": albums}


@router.get("/music-store/api/v1/singer/{id}")
async def get_tracks_artist(id):
    songs = get_songs_artist(id)
    return {"songs": songs}
