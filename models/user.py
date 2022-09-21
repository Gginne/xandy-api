import email
from enum import unique
from sqlalchemy import Column, String
from config.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True, unique=True)
    name = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(100))

    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        

    def __repr__(self):
        return f"<User '{self.name}' : {self.id}>"