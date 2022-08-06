from database  import db

class Usuario(db.Model):
    id = db.column(db.Integer, primary_Key=True)
    nome  = db.Column(db.String(180), unique=False, nulable=False)
    username = db.Column(db.String(120), unique=True, nulable=False)
    email = db.Column(db.String(180), unique=True, nulable=True) 
    telefone = db.Column(db.String(40), unique=False, nulable=True)
    senha = db.column(db,String(100), unique=False, nulable=False)
