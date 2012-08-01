# -*- coding: utf-8 -*-

import unittest
import gangape


class UsersTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_create(self):
        name = 'YoLo'
        email = 'gatorade@bitch.me'
        password = 'yolo123'

        assertEqual(Users.create_user(email=email),
                    (u'Fail', u'Missing Parameters'))

        assertEqual(Users.create_user(email=email, password=password),
                    (u'OK', u'Missing Parameters'))

        assertEqual(Users.create_user(email=email, password=password,
                                      name=name, photo=photo),
                    (u'OK', u'Missing Parameters'))


    def test_update_user(self):
        pass

class ProductsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class APITestCase(unittest.TestCase):

    def setUp(self):
        """
        Load test database
        """
        pass

    def tearDown(self):
        """
        Destoy test database
        """
        pass

if __name__ == '__main__':
    unittest.main()
