from application import app
from flask import jsonify
from random import choice

races = ['human', 'elves', 'halflings', 'dwarves', 'dragonborm']

@app.route('/get-race', methods=['GET'])
def get_race():
    race = choice(races)
    return jsonify(race=race)