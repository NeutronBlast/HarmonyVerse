from fastapi import APIRouter

from repositories.track_repository import get_song

router = APIRouter()


@router.get("/music-store/api/v1/song/{id}")
async def get_song_detail(id):
    """Returns the details about a specific song

    Parameters
    ----------
    id : int
        Song ID

    Returns
    ------
    dict
        Song details
    """
    song = get_song(id)
    return {"song": song}
