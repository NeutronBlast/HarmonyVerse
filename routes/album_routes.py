from fastapi import APIRouter

from repositories.album_repository import get_songs_album

router = APIRouter()


@router.get("/music-store/api/v1/albums/{id}")
async def get_tracks_album(id):
    """Returns all the tracks from an album

    Parameters
    ----------
    id : int
        Album ID

    Returns
    ------
    list
        List of songs that belong to an album
    """
    songs = get_songs_album(id)
    return {"songs": songs}
