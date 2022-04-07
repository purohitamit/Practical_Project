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
    def test_get_weapon_human(self):
        response = self.client.post(url_for('get_weapon'), json={'race':'Human', 'claas':'Barbarian'})
        self.assert200(response)
        self.assertIn(b'Longsword', response.data)
        
    def test_get_weapon_elves(self):
        response = self.client.post(url_for('get_weapon'), json={'race':'Elves', 'claas':'Barbarian'})
        self.assert200(response)
        self.assertIn(b'Warhammers', response.data)
