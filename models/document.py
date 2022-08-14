from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from config.db import Base

class Document(Base):
    __tablename__ = 'documents'
    id = Column(String(32), primary_key=True, unique=True)
    format = Column(String(50))
    book = relationship("Book", back_populates="document")
    
    def __init__(self, id=None, format=None):
        self.id = id
        self.format = format

    def __repr__(self):
        return f'<Document {self.id!r}>'