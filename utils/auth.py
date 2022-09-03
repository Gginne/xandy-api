from flask import request, jsonify
from functools import wraps

import os
import jwt

from models import user


def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, os.environ['JWT_SECRET_KEY'], algorithms=['HS256'])
            current_user = user.User.query.filter_by(id=data['user_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
   return decorator