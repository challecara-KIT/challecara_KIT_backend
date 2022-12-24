from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db.model import Base
from routers.main import router

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

app.include_router(router, prefix="/api/v1")
