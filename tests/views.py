# -*- coding: utf-8 -*-

import unittest
from flask.ext.sqlalchemy import SQLAlchemy
from ganga import app

class GangaAPI(unittest.TestCase):
    def setUp(self):
        app.config.from_object('settings')
        self.db = SQLAlchemy(app)
        self.db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_create_user_missing_password(self):
        data = { 'email': 'pirata@gmail.com', }
        response = self.client.put('/user/', data=data)
        assert response.status_code, 200

    def test_create_user_missing_email(self):
        data = { 'email': '',
                 'password': 123, }
        response = self.client.put('/user/', data=data)
        assert response.status_code, 200

    def test_create_user_successfully(self):
        data = { 'email': 'pirata@gmail.com',
                 'password': 123, }
        response = self.client.put('/user/', data=data)
        assert response.status_code, 200

    def test_create_user_duplicate(self):
        data = { 'email': 'pirata@gmail.com',
                 'password': 123, }
        response = self.client.put('/user/', data=data)
        assert response.status_code, 400

if __name__ == '__main__':
    unittest.main()
