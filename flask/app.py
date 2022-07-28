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

@app.route('/chave/cadastrar')
def cadastrar_chave():
   return ("Nao implementado")

@app.route('/chave/listar')
def listar_chaves():
   return ("Nao implementado")

@app.route('/usuario/listar')
def listar_usuarios():
   return ("Nao implementado")

@app.route('/usuario/cadastrar')
def cadastrar_usuario():
   return ("Nao implementado")

@app.route('/chave/emprestar')
def emprestar_chave():
   return ("Nao implementado")

@app.route('/chave/listar_emprestimos')
def listar_emprestimos():
   return ("Nao implementado")

@app.route('/chave/devolver')
def devolver_chave():
   return ("Nao implementado")