from fastapi import APIRouter

from repositories.track_repository import get_song

router = APIRouter()


@router.get("/music-store/api/v1/song/{id}")
async def get_song_detail(id):
    song = get_song(id)
    return {"song": song}
