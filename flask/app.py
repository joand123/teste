from flask import Flask
from waitress import serve
from flask import render_template
from flask import request,url_for,redirect,flash,session
import logging

app = Flask(__name__)

logging.basicConfig(filename='/flask/app.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

@app.route('/')
def root():
   return (render_template('index.html'))

@app.route('/chave/cadastrar',methods=['POST','GET'])
def cadastrar_chave():
   form = ChaveForm()
   if form.validate_on_submit():
       #PROCESSAMENTO DOS DADOS RECEBIDOS
       app.logger.debug(u'AQUI VEM A IMPLEMENTAÇÃO DO CADASTRO DA CHAVE')
       app.logger.debug(request.form['nome'])
       return(redirect(url_for('root')))
   return (render_template('form.html',form=form,action=url_for('cadastrar_chave')))

@app.route('/chave/listar')
def listar_chaves():
   return ("Nao implementado")

@app.route('/usuario/listar')
def listar_usuarios():
   return ("Nao implementado")

@app.route('/usuario/cadastrar',methods=['POST','GET'])
def cadastrar_usuario():
   form = UsuarioForm()
   if form.validate_on_submit():
       #PROCESSAMENTO DOS DADOS RECEBIDOS
       app.logger.debug(u'AQUI VEM A IMPLEMENTAÇÃO DO CADASTRO DE USUÁRIO')
       app.logger.debug(request.form['nome'])
       return(redirect(url_for('root')))
   return (render_template('form.html',form=form,action=url_for('cadastrar_usuario')))

@app.route('/chave/emprestar')
def emprestar_chave():
   return ("Nao implementado")

@app.route('/chave/listar_emprestimos')
def listar_emprestimos():
   return ("Nao implementado")n 

@app.route('/chave/devolver')
def devolver_chave():
   return ("Nao implementado")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' = CSV_DIR ='bd.sqlite3'
app.config['SQLALCHEMY_TTRACK-MODIFICATIONS'] = False
db.init_app(app)

from Usuarios import Usuarios
fro, Chaves import Chaves

@app.before_first_request
def inicializar_bd() :
   db.create_all()

@app.route('/')
def root():
