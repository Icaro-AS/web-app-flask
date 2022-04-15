from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao import LivroDao, UsuarioDao
from models import Livro, Usuario
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'setechaves'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Aleteia7*"
app.config['MYSQL_DB'] = "livraria"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

livro_dao = LivroDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    lista = livro_dao.listar()
    return render_template('lista.html', titulo='Livros', livros=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('cadastro.html', titulo='Novo Livro')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    autor = request.form['autor']
    livro = Livro(nome, categoria, autor)
    livro_dao.salvar(livro)
    return redirect(url_for('index'))



@app.route('/editar')
def editar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    return render_template('editar.html', titulo='Editar Livro')

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    return render_template('editar.html', titulo='Alteração de Livro')



@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'] )
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.id
            flash(request.form['usuario'] + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)
