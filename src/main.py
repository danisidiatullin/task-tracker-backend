import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

import database
import schemas
from endpoints import tasks, users

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


@app.get("/api/task_statuses", status_code=200)
async def statuses():
    return [e.value for e in schemas.StatusEnum]


app.include_router(users.router)
app.include_router(tasks.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0")
