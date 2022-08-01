import cProfile
from enum import unique
from ssl import _PasswordType
from unicodedata import name
from database  import db

class Usuario(db.Model):
    id = db.column(db.Integer, primary_Key=True)
    name = db.Column(db.String(180), unique=False, nulable=False)
    username = db.Column(db.String(120), unique=True, nulable=False)
    cpf = db.Column(db.String(100), unique=True, nulable=True) 
    password = db.Column(db.String(100), unique=False, nulable=False) 
    email = db.Column(db.String(180), unique=True, nulable=True) 