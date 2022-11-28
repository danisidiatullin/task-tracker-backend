import fastapi

from fastapi import security

from sqlalchemy import orm
from fastapi.middleware.cors import CORSMiddleware

import database


app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database.Base.metadata.create_all(bind=database.engine)








@app.get("/api", status_code=200)
async def root():
    return {"message": "Task Tracker"}




