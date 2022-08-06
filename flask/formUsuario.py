from flask-wtf import Flaskform
from wtforms import StrinField,SubmitField,PassworField
from wtforms.field.html5 import EmailField
from wtforms.Validators import DataRequired

class  UsuariosForms(FlaskForms):
    nome = StringField('Nome da Chave: ' , validators=[DataRequired()])
    username =  StringField('Nome do Usuario: ', validator=[dataRequred()])
    telefone = StringField('telefone: ', validator=[dataRequred()])
    senha = StringField('Senha: ', validator=[dataRequred()])
    enviar = SubmitField('CADASTRAR')
    
