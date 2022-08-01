from database import db

class Chave(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String, unique=False, nulable=False)