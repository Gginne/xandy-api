from enum import unique
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(String(36), primary_key=True, unique=True)
    isbn = Column(String(13), unique=True)
    title = Column(String(100), unique=True)
    file_id = Column(String(36), ForeignKey("files.id"))
    file = relationship("File", uselist=False, backref="document")

    def __init__(self, id=None,isbn=None, title=None, file_id=None):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.file_id = file_id

    def __repr__(self):
        return f"<Book '{self.title}'>"