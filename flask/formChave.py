from flask-wtf import Flaskform
from wtforms import StrinField, SubmitField
from wtforms, Validators import DataRequired

class  ChaveForms(FlaskForms):
    nome = StringField('Nome da Chave' , validators=[DataRequired()])
    enviar = SubmitField(CADASTRAR)