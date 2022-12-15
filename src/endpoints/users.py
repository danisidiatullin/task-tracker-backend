import fastapi
from fastapi import APIRouter, security
from sqlalchemy import orm

import schemas
import services

router = APIRouter(tags=["users"])


@router.post("/api/users")
async def create_user(user_data: schemas.UserCreate, db: orm.Session = fastapi.Depends(services.get_db)):
    db_user = await services.get_user_by_email(user_data.email, db)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email already created")

    user = await services.create_user(user_data, db)

    return await services.create_token(user)


@router.post("/api/token")
async def generate_token(
    form_data: security.OAuth2PasswordRequestForm = fastapi.Depends(),
    db: orm.Session = fastapi.Depends(services.get_db),
):
    user = await services.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")

    return await services.create_token(user)


@router.get("/api/users/me", response_model=schemas.User)
async def get_user(user: schemas.User = fastapi.Depends(services.get_current_user)):
    return user
