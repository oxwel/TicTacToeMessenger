from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fb_id = db.Column(db.Integer, unique=True)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    ties = db.Column(db.Integer, default=0)
    games = db.Column(db.Integer, default=0)

    def __init__(self, fb_id):
        self.fb_id = fb_id
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.games = 0