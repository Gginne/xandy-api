from flask import request,jsonify,make_response

import uuid

from config.db import db_session as session
from models import collection
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
