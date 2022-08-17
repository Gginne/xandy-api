from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from config.db import Base

class File(Base):
    __tablename__ = 'files'
    id = Column(String(32), primary_key=True, unique=True)
    format = Column(String(50))
    
    def __init__(self, id=None, format=None):
        self.id = id
        self.format = format

    def __repr__(self):
        return f'<File {self.id!r}>'