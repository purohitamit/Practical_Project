from application import app, db
from flask import Flask, render_template, request, url_for
from application.models import Characters
import requests
@app.route('/')
def home():
    race = requests.get('http://race:5000/get-race')
    claas = requests.get('http://claas:5000/get-claas')
    weapon = requests.post('http://weapon:5000/get-weapon', json={"race":race.json()["race"], "claas":claas.json()["claas"]})
    new_character = Characters(race=race.json()["race"], claas=claas.json()["claas"], weapon=weapon.json()["weapon"])
    db.session.add(new_character)
    db.session.commit()
    past5 = Events.query.order_by(Characters.id.desc()).limit(5).all()
    return render_template("index.html", race=race.json()["race"], claas=claas.json()["claas"], weapon=weapon.json()["weapon"], past5=past5.json()["past5"])

@app.route('/history', methods=['GET'])
def history():
    character_history = Characters.query.all()
    return render_template("history.html", character_history = character_history)