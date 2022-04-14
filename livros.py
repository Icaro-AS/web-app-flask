from flask import Flask, render_template, request,redirect

class Livro:
    def __init__(self,nome,categoria,autor):
        self.nome = nome
        self.categoria = categoria
        self.autor = autor


livro1 = Livro('O senhor dos anéis', 'Fantasia', 'J.R.R Tolkien')
livro2 = Livro('Cristianismo Puro e Simples', 'Filosofia', 'C.S Lewis')
livro3 = Livro('Ortodoxia', 'Filosofia', 'G.K Chesterton')
lista = [livro1, livro2, livro3]


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('lista.html', titulo='Livros', livros=lista)


@app.route('/novo')
def novo():
    return render_template('cadastro.html', titulo='Novo Livro')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    autor = request.form['autor']
    livro = Livro(nome, categoria, autor)
    lista.append(livro)
    return redirect('/')
app.run(debug=True)
