from flask import url_for
from flask_testing import TestCase
from datetime import date
import requests_mock
import pytest
from application import app, db
from application.models import Characters


class TestBase(TestCase):
     def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", DEBUG=True)
        return app
    
     def setUp(self):
        sample_character= Characters(race='Human', claas='Bard', weapon='Whip')
        db.create_all()
        db.session.add(sample_character)
        db.session.commit()

     def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_character(self):
        with requests_mock.Mocker() as m:
            m.get('http://race:5000/get-race', json={'race':'Dwarves'})
            m.get('http://claas:5000/get-claas', json={'claas':'Fighter'})
            m.post('http://weapon:5000/get-weapon', json={'weapon':'Warhammers'})
            response = self.client.get(url_for('home'))
            self.assert200(response)
            self.assertIn(b'Your fantasy role was Human Race from the Bard Class and you fought with Whip', response.data)
            self.assertIn(b'Your fantasy role was Dwarves Race from the Fighter Class and you fought with Warhammers', response.data)
    def test_hist_get(self):
        response = self.client.get(url_for('history'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Human', response.data)