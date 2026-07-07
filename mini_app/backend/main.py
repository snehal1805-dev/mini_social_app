from fastapi import FastAPI

from database import engine
from database import Base

from routes.auth_routes import router as auth_router
from routes.post_routes import router as post_router

from models.user_model import User
from models.post_model import Post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


Base.metadata.create_all(bind=engine)


app.include_router(auth_router)

app.include_router(post_router)


@app.get("/")
def home():

    return {
        "message": "Social Media API 🚀"
    }
