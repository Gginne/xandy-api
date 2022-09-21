from enum import unique
from sqlalchemy import Table, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base


class Collection(Base):
    __tablename__ = 'collections'
    id = Column(String(36), primary_key=True, unique=True)
    name = Column(String(50), unique=True)
    books = relationship("BookCollection",  back_populates="collection")

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        

    def __repr__(self):
        return f"<Collection '{self.name}' : {self.id}>"