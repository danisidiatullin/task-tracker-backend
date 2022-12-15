import os
import pathlib
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Tracker"

    POSTGRES_USER: Optional[str] = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: Optional[str] = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: Optional[str] = os.getenv("POSTGRES_DB")

    SECRET: str = os.getenv("SECRET", "")

    class Config:
        env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"


settings = Settings()
