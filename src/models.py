from passlib import hash
from sqlalchemy import Column, Integer, String, orm

import database


class User(database.Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def verify_password(self, password: str):
        return hash.bcrypt.verify(password, self.hashed_password)
