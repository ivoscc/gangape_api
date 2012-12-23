# -*- coding: utf-8 -*-

import simplejson as json
from flask import jsonify
from gangape import app
from gangape.models import Users, Products


@app.route('/user/', methods=['POST'])
def create_user():
    """
    Create a new user.
    Returns: the user_id
    
    Required Parameters: email and password.
    Optional Parameters: photo, name
    """

    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    photo = request.form.get('photo')

    if None in (email, password):
        return json.dumps(
            {'status': 'Error. Missing required parameters',
             'debug-info': 'Supplied parameters.'
             'email: %s, password: %s.' % (email, password),}
            )
    
    user_id = Users.create_user(
        email=email,
        password=password,
        name=name,
        photo=photo,
        )
    
    return jsonify(user_id=user_id)


@app.route('/user/login/', methods=['GET'])
def login_check():
    """
    An end_point to Check of the Basic Auth Credentials are valid
    """
    return "Oh Hai"


@app.route('/user/<int:user_id>/', methods=['GET'])
def get_user():
    return "Oh Hai"


if __name__ == "__main__":
    app.run(debug=True)  # Change to false in production?
