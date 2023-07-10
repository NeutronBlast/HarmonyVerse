from fastapi import FastAPI
from routes.artist_routes import router as artist_router
from routes.album_routes import router as album_router
from routes.track_routes import router as track_router

app = FastAPI()

app.include_router(artist_router)
app.include_router(album_router)
app.include_router(track_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
