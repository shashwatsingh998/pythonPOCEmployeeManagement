import os
from werkzeug.security import generate_password_hash
from flask_pymongo import PyMongo
import unittest
from flask_testing import TestCase
from flask import url_for
from dotenv import load_dotenv
from inventory import create_app

load_dotenv()
class ViewsTestCase(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['MONGO_URI'] = os.getenv('TEST_MONGO_URI')
        self.mongo=PyMongo(app)
        print(os.getenv('TEST_MONGO_URI'))
        print(app.config['MONGO_URI'])

        return app

    def setUp(self):
        self.mongo.db.users.delete_many({})

    def tearDown(self):
        self.mongo.db.users.delete_many({})

    def test_index(self):
        response=self.client.get(url_for('main.index'))
        self.assertStatus(response,302)

if __name__ == '__main__':
    unittest.main()
