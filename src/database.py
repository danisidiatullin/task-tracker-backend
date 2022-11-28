import sqlalchemy
from sqlalchemy.ext import declarative
import sqlalchemy.orm as orm

from config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}"
    f"@task-tracker-postgres/"
    f"{settings.POSTGRES_DB}"
)

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()

