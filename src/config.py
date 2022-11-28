import os
import pathlib

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Tracker"
    sqlalchemy_database_url: str = os.getenv("SQLALCHEMY_DATABASE_URL")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")

    SECRET: str = os.getenv("SECRET")

    class Config:
        env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"


settings = Settings()
