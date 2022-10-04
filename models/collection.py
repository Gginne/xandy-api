from enum import unique
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base


class Collection(Base):
    __tablename__ = 'collections'
    id = Column(String(36), primary_key=True, unique=True)
    name = Column(String(50), unique=True)
    user_id = Column(String(36), ForeignKey("users.id"))
    
    books = relationship("BookCollection",  back_populates="collection")
    user = relationship("User", uselist=False, backref="collection")
    
    def __init__(self, id=None, name=None, user_id=None):
        self.user_id = user_id
        self.id = id
        self.name = name
        

    def __repr__(self):
        return f"<Collection '{self.name}' : {self.id}>"