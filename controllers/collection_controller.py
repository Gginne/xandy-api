from flask import request,jsonify,make_response
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound

import uuid

from config.db import db_session as session
from models import collection, book
from utils import auth

@auth.token_required
def create_collection(user):
    data = dict(request.form)

    #Create collection id
    collection_id = uuid.uuid4()
      
    # Create book row from data
    new_collection = collection.Collection(id=collection_id, name=data['name'], user_id=user.id)
    
    #Add file and new book
    session.add(new_collection)
    session.commit()
    
    return make_response(jsonify({
            "message": f"Successfully Created Collection '{data['name']}'",
    }))

@auth.token_required
def add_book(user, collection_id):
    data = dict(request.form)
    
    book_id = data['book_id']
    
    bk = None
    coll = None
    try:
        bk = session.query(
                book.Book
        ).filter(
                and_(book.Book.id==book_id, book.Book.user_id == user.id)
        ).one()
   
    # Deal with it
    except NoResultFound:
        return make_response(jsonify({
            "message": "book not found",
        }), 404)
    
    try:
        coll = session.query(
                collection.Collection
        ).filter(
                and_(collection.Collection.id==collection_id, collection.Collection.user_id == user.id)
        ).one()
    # Deal with it
    except NoResultFound:
        return make_response(jsonify({
            "message": "collection not found",
        }), 404)

   
    coll.books.append(bk)
    
    session.commit()
    
    return make_response(jsonify({
         "message": f"Successfully Added Book '{bk.title}' to Collection '{coll.name}'",
    }))
    
        