from application import app
from flask import jsonify
from flask import request, Response

@app.route('/get-weapon', methods=['POST'])
def get_weapon():
    weapons = {
        "Human" : {
            "Barbarian" : "Longsword",
            "Bard" : "Whip",
            "Fighter" : "Trident",
            "Monk" : "Longbows",
            "Ranger" : "Warhammers"
        },
        "Elves" : {
             "Barbarian" : "Warhammers",
            "Bard" : "Longsword",
            "Fighter" : "Whip",
            "Monk" : "Trident",
            "Ranger" : "Longbows"
        },
        "Halflings" : {
             "Barbarian" : "Longbows",
            "Bard" : "Warhammers",
            "Fighter" : "Longsword",
            "Monk" : "Whip",
            "Ranger" : "Trident"
        },
        "Dwarves" : {
             "Barbarian" : "Trident",
            "Bard" : "Longbows",
            "Fighter" : "Warhammers",
            "Monk" : "Longsword",
            "Ranger" : "Whip"
        },
        "Dragonborm" : {
             "Barbarian" : "Whip",
            "Bard" : "Trident",
            "Fighter" : "Longbows",
            "Monk" : "Warhammers",
            "Ranger" : "Londsword"
        },
    }
    data = request.get_json()
    weapon = weapons[data["race"]][data["claas"]]
    return jsonify(weapon=weapon)
