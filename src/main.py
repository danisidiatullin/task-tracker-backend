import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

import database
from endpoints import users

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


app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0")
