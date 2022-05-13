from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import database


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://0.0.0.0:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# async def startup():
#     await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def index():
    return {"status": 'ok'}


# app.include_router(user.router, prefix="/user", tags=["user"])


# uvicorn main:app --reload
