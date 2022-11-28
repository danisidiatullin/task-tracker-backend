import fastapi
from fastapi import APIRouter
from sqlalchemy import orm

import schemas
import services

router = APIRouter(tags=["tasks"])


@router.post("/api/tasks", response_model=schemas.Task)
async def create_task(
    task: schemas.TaskCreate,
    user: schemas.User = fastapi.Depends(services.get_current_user),
    db: orm.Session = fastapi.Depends(services.get_db),
):
    return await services.create_task(user=user, db=db, task=task)


@router.get("/api/tasks", response_model=list[schemas.Task])
async def get_tasks(
    user: schemas.User = fastapi.Depends(services.get_current_user),
    db: orm.Session = fastapi.Depends(services.get_db),
):
    return await services.get_tasks(user=user, db=db)


@router.get("/api/tasks/{task_id}", status_code=200)
async def get_task(
    task_id: int,
    user: schemas.User = fastapi.Depends(services.get_current_user),
    db: orm.Session = fastapi.Depends(services.get_db),
):
    return await services.get_task(task_id, user, db)


@router.delete("/api/tasks/{task_id}", status_code=204)
async def delete_task(
    task_id: int,
    user: schemas.User = fastapi.Depends(services.get_current_user),
    db: orm.Session = fastapi.Depends(services.get_db),
):
    await services.delete_task(task_id, user, db)
    return {"message": "Successfully Deleted"}


@router.put("/api/tasks/{task_id}", status_code=200)
async def update_task(
    task_id: int,
    task: schemas.TaskCreate,
    user: schemas.User = fastapi.Depends(services.get_current_user),
    db: orm.Session = fastapi.Depends(services.get_db),
):
    await services.update_task(task_id, task, user, db)
    return {"message": "Successfully Updated"}
