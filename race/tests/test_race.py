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

    def test_get_race(self):
       with patch('application.routes.choice') as r:
           r.return_value = 'Human'
           response = self.client.get(url_for('get_race'))
           self.assert200(response)
           self.assertIn(b'Human', response.data)

    def test_get_race2(self):
       with patch('application.routes.choice') as r:
           r.return_value = 'Elves'
           response = self.client.get(url_for('get_race'))
           self.assert200(response)
           self.assertIn(b'Elves', response.data)