import boto3
import uuid
import os

from config.db import db_session as session
from models import book, document

s3 = boto3.client('s3')

def create_book(data):
    
    doc_id = uuid.uuid4()
    # Create document row from data and assign uuid as id
    new_doc = document.Document(id=doc_id, format='PDF')
    # Create book row from data
    new_book = book.Book(title=data['title'], isbn=data['isbn'], doc_id=doc_id)
    
    #Add document and new book
    session.add(new_doc)
    session.add(new_book)
    session.commit()
    
    # Upload file to bucket using S3
    s3.upload_file(
        Filename=data['filename'],
        Bucket=os.environ['DOCUMENT_BUCKET'],
        Key=f'{doc_id}',
    )
    
