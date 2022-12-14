from enum import Enum

import pydantic


class UserBase(pydantic.BaseModel):
    email: str


class UserCreate(UserBase):
    hashed_password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class StatusEnum(str, Enum):
    STARTED = "started"
    PENDING = "pending"
    FINISHED = "finished"


class TaskBase(pydantic.BaseModel):
    title: str
    description: str
    priority: int
    progress: int
    status: StatusEnum = StatusEnum.STARTED


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
