from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
import application.routes
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):

    def test_get_claas(self):
       with patch('application.routes.choice') as r:
           r.return_value = 'Barbarian'
           response = self.client.get(url_for('get_claas'))
           self.assert200(response)
           self.assertIn(b'Barbarian', response.data)

    def test_get_claas2(self):
       with patch('application.routes.choice') as r:
           r.return_value = 'Bard'
           response = self.client.get(url_for('get_claas'))
           self.assert200(response)
           self.assertIn(b'Bard', response.data)