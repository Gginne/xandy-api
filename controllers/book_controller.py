import boto3
from flask import request,jsonify,make_response
from sqlalchemy import and_
from werkzeug.utils import secure_filename

import os
import uuid

from config.db import db_session as session
from models import book, file
from utils import auth


@auth.token_required
def upload_book(user):
    
    data = dict(request.form)
    data['file'] = request.files.get("file")

    book_id = uuid.uuid4()
    file_id = uuid.uuid4()
    # Create document row from data and assign uuid as id
    new_file = file.File(id=file_id, format='PDF')
    # Create book row from data
    new_book = book.Book(id=book_id, title=data['title'], isbn=data['isbn'], file_id=file_id, user_id=user.id)
    
    #Add file and new book
    session.add(new_file)
    session.add(new_book)
    session.commit()
    
    # Upload file to bucket using S3
    if _upload_file_to_s3(data['file'], file_id):
        return make_response(jsonify({
            "message": f"Successfully Uploaded Book '{data['title']}'",
        }))
    
    return make_response(jsonify({
            "message": f"Failed To Upload Book '{data['title']}'",
    }), 500)


@auth.token_required
def read_book(user, book_id): 

    q_book = session.query(
        book.Book
    ).filter(
        and_(book.Book.id == book_id, book.Book.user_id == user.id)
    ).first()
    
    if q_book == None:
        return make_response(jsonify({
            "message": 'book not found',
        }), 404)
    
    book_file = None
    
    try:
        book_file = _load_file_from_s3(q_book.file_id)
    except:
        return make_response(jsonify({
            "message": 'failed to load book',
        }), 500)
    
    response = make_response(book_file['Body'].read())
    response.headers['Content-Type'] = 'application/pdf'
    return response


@auth.token_required
def search_books(user):
    
    q_title = f"%{request.args.get('q')}%"
    
    books = session.query(
        book.Book
    ).filter(
        and_(book.Book.title.like(q_title), book.Book.user_id == user.id)
    ).all()
    
    books = [_serialize_book(b) for b in books]

    return make_response(jsonify(books))

    
def _serialize_book(book_obj):
    return {
        'id': book_obj.id,
        'isbn': book_obj.isbn,
        'title': book_obj.title
    }
    
def _load_file_from_s3(file_id):
    s3 = boto3.client('s3')
    
    try:
        file = s3.get_object(
            Bucket=os.environ['DOCUMENT_BUCKET'], 
            Key=file_id
        )
        
        return file
       
    
    except Exception as e:
        print("Failed to load file from bucket: ", e)
        return False
    
def _upload_file_to_s3(file, file_id):
    s3 = boto3.client('s3')
    
    try:
        file.filename = secure_filename(file.filename)
        s3.upload_fileobj(
            Fileobj=file,
            Bucket=os.environ['DOCUMENT_BUCKET'],
            Key=f'{file_id}',
        )
        
    except Exception as e:
        print("Failed to upload file to bucket: ", e)
        return False
    
    print("Uploaded {}".format(file.filename))
    return True
        