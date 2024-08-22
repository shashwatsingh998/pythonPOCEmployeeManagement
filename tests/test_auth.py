import unittest
import os
import sys
from flask_testing import TestCase
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from inventory import create_app
from inventory.db import mongo
from werkzeug.security import generate_password_hash

load_dotenv()

class AuthTestCase(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['MONGO_URI'] = os.getenv('TEST_MONGO_URI')
        self.mongo=PyMongo(app)
        return app

    def setUp(self):
        self.mongo.db.users.delete_many({})

    def tearDown(self):
        self.mongo.db.users.delete_many({})

    def test_register(self):
        response = self.client.post('/register', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=False)
        self.assertRedirects(response,'/login')

    def test_login(self):
        self.mongo.db.users.insert_one({
            'username': 'testuser',
            'password': generate_password_hash('testpassword')
        })
        response = self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        self.assertIn(b'<h1>Employee List</h1>', response.data)

    def test_invalid_login(self):
        response = self.client.post('/login', data=dict(
            username='wronguser',
            password='wrongpassword'
        ), follow_redirects=True)
        self.assertIn(b'<p>Invalid username or password please try again later</p>', response.data)

    def test_logout(self):
        self.mongo.db.users.insert_one({
            'username': 'testuser',
            'password': generate_password_hash('testpassword')
        })
        self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'<h1>Login</h1>\n<form method="POST">', response.data)

if __name__ == '__main__':
    unittest.main()
