from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db.model import Base
from routers.main import router
from utils.image import tagging_image

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ひまじんのたまり場"
)


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def hello():
    return {"message": "Hello Challecara!"}

@app.get('/tagging')
async def tag_image(image_url: str):
    tagging_image(image_url)
    return {"message": "done"}

app.include_router(router, prefix="/api/v1")
