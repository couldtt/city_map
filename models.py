from init import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(64), unique=True)
    population = db.Column(db.Integer, nullable=False, default=0)
