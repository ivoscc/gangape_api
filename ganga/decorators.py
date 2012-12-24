# -*- coding: utf-8 -*-

from functools import wraps
from base64 import b64decode
from flask import (request, make_response, redirect, jsonify, g)
from ganga.models import User

def authentication_required(f):
    """Basic Authorization assumed
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if auth_header is None:
            return jsonify({'error': 'Please set the authorization header'}), 401

        auth_type, key = auth_header.split(' ')
        if auth_type != "Basic":
            return jsonify({'error': 'Only Basic Auth is supported'}), 401

        if key is None:
            return jsonify({'error': 'No username or password supplied'}), 400
        
        email, password = b64decode(key).split(':')

        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({'error': 'The email %s is not registered' % (email,)}), 401
        elif user.password == password:
            g.user = user
        else:
            return jsonify({'error': 'No wrong password'}), 401

        return f(*args, **kwargs)
    return decorated_function
