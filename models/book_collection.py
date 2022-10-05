from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base


class BookCollection(Base):
    __tablename__ = "book_collections"
    book_id = Column(String(36), ForeignKey("books.id"), primary_key=True)
    collection_id = Column(String(36), ForeignKey("collections.id"), primary_key=True)
    
