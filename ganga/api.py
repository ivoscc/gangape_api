# -*- coding: utf-8 -*-

import simplejson as json
from flask import jsonify, request, g
from ganga import app, db
from ganga.models import User, Product
from ganga.decorators import authentication_required


@app.route('/users/', methods=['PUT'])
def create_user():
    """
    Create a new user.
    Returns: the user_id
    
    Required Parameters: email and password.
    Optional Parameters: photo, name
    """

    email = request.form.get('email', None)
    password = request.form.get('password', None)

    if None in (email, password):
        return jsonify(
            {'status': 'Error. Missing required parameters',
             'debug-info': 'Supplied parameters.'
             'email: %s, password: %s.' % (email, password),}
            )
    
    user = User(email=email, password=password, )
    db.session.add(user)
    db.session.commit()
    
    return jsonify(user_id=user.id)


@app.route('/user/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    return jsonify(User.query.filter_by(id=user_id).first().as_json)

@app.route('/users/<int:user_id>/', methods=['GET'])
def display_user():
    return jsonify({'message': 'I O U'}), 501


@app.route('/user/check_credentials/', methods=['GET'])
@authentication_required
def login_check():
    """
    An end_point to Check of the Basic Auth Credentials are valid
    """
    return jsonify(g.user.as_json)

@app.route('/product', methods=['PUT'])
def create_product():
    pass


if __name__ == "__main__":
    app.run(debug=True)  # Change to false in production?
