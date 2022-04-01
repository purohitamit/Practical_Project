from application import app
from flask import jsonify
from random import choice

races = ['Human', 'Elves', 'Halflings', 'Dwarves', 'Dragonborm']

@app.route('/get-race', methods=['GET'])
def get_race():
    race = choice(races)
    return jsonify(race=race)