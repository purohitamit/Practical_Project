from application import db

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(50))
    claas = db.Column(db.String(50))
    weapon = db.Column(db.String(50))
   