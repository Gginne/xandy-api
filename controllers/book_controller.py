import boto3
from flask import request,jsonify

import uuid
import os

from config.db import db_session as session
from models import book, file
from werkzeug.utils import secure_filename


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

def upload_book(data=None):
    
    if data == None:
        data = dict(request.form)
        data['file'] = request.files.get("file")

    file_id = uuid.uuid4()
    # Create document row from data and assign uuid as id
    new_file = file.File(id=file_id, format='PDF')
    # Create book row from data
    new_book = book.Book(title=data['title'], isbn=data['isbn'], file_id=file_id)
    
    #Add file and new book
    session.add(new_file)
    session.add(new_book)
    session.commit()
    
    # Upload file to bucket using S3
    if _upload_file_to_s3(data['file'], file_id):
        return jsonify({
            "message": f"Successfully Uploaded Book '{data['title']}'",
        })
    
    return jsonify({
            "message": f"Failed To Upload Book '{data['title']}'",
    })

    
    
