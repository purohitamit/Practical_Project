from application import app
from flask import jsonify
from random import choice

claases = ['Barbarian', 'Bard', 'Fighter', 'Monk', 'Ranger']

@app.route('/get-claas', methods=['GET'])
def get_claas():
    claas = choice(claases)
    return jsonify(claas=claas)