from flask import request,jsonify,make_response
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

import os
import uuid
import jwt
import datetime

from config.db import db_session as session
from models import user

def _serialize_user(user_obj):
    return {
        'id': user_obj.id,
        'name': user_obj.name,
        'email': user_obj.email
    }
    
def register_user():
    
    user_data = dict(request.form)
    
    id = uuid.uuid4()
    name = user_data['name']
    email = user_data['email']
    password_hash = generate_password_hash(user_data['password'], method='sha256')
    
    new_user = user.User(id=id, name=name, email=email, password=password_hash) 
    
    try:
        session.add(new_user)  
        session.commit()  
        
        return jsonify({
            'message': 'registered successfully'
        }) 
        
    except IntegrityError:
        
        session.rollback()
        
        return jsonify({
            'message': 'Duplicate name or email',
        }) 
        
    
def login_user():
   
    auth = request.authorization   

    if not auth or not auth.username or not auth.password:  
        return make_response('missing username or password', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    
    
    current_user = user.User.query.filter_by(name=auth.username).first()  
    
    if current_user is None:
        return make_response('user not found',  404, {'WWW.Authentication': 'Basic realm: "login required"'})
    
    if check_password_hash(current_user.password, auth.password):  
        token = jwt.encode({'user_id': current_user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, os.environ['JWT_SECRET_KEY'])  
        return jsonify({'token' : token}) 
    
    return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})