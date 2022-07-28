from flask-wtf import Flaskform
from wtforms import StrinField,SubmitField,PassworField
from wtforms,Validators import DataRequired

class  UsuariosForms(FlaskForms):
    nome = StringField('Nome da Chave' , validators=[DataRequired()])
    username =  StringField('Nome do Usuario')
    senha = StringField('Senha: ')
    enviar = SubmitField('CADASTRAR')
    