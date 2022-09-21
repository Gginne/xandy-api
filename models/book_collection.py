from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class BookCollection(Base):
    __tablename__ = "book_collections"
    book_id = Column(ForeignKey("books.id"), primary_key=True)
    collection_id = Column(ForeignKey("collections.id"), primary_key=True)
    
    book = relationship("Book", back_populates="collections")
    collection = relationship("Collection", back_populates="books")
