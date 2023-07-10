from fastapi import APIRouter

from repositories.album_repository import get_songs_album

router = APIRouter()


@router.get("/music-store/api/v1/albums/{id}")
async def get_tracks_album(id):
    songs = get_songs_album(id)
    return {"songs": songs}
