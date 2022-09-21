import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = os.environ.get('DB_URL', 'mysql://root:@127.0.0.1:3306/xandy')
engine = create_engine(DB_URL)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Import models
    import models.file
    import models.book
    import models.user
    import models.collection
    import models.book_collection
    Base.metadata.create_all(bind=engine)