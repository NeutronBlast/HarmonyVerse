from fastapi import APIRouter

from repositories.artist_repository import get_all_artists

router = APIRouter()


@router.get("/music-store/api/v1/singers")
async def get_artists():
    artists = get_all_artists()
    return {"artists": artists}
