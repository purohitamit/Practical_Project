from application import app
from flask import Flask, render_template, request
import requests
@app.route('/')
def index():
    race = requests.get('http://race:5000/get-race')
    claas = requests.get('http://claas:5000/get-claas')
    weapon = requests.post('http://weapon:5000/get-weapon', json={"race":race.json()["race"], "claas":claas.json()["claas"]})
    return render_template("index.html", race=race.json()["race"], claas=claas.json()["claas"], weapon=weapon.json()["weapon"])
