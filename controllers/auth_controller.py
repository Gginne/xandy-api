from flask import request,jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

import uuid

from config.db import db_session as session
from models import user

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
            'message': 'registered successfully',
            'user': {
                'id': id,
                'name': name, 
                'email': email,
                'password': user_data['password']
            }
        }) 
        
    except IntegrityError:
        
        session.rollback()
        
        return jsonify({
            'message': 'Duplicate name or email',
        }) 
        
    
    
     

   