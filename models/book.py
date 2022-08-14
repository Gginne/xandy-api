from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base

class Book(Base):
    __tablename__ = 'books'
    isbn = Column(String(17), primary_key=True)
    title = Column(String(100), unique=True)
    doc_id = Column(String(32), ForeignKey("documents.id"))
    document = relationship("Document", back_populates="book")

    def __init__(self, isbn=None, title=None, doc_id=None):
        self.isbn = isbn
        self.title = title
        self.doc_id = doc_id

    def __repr__(self):
        return f'<Book {self.title!r}>'