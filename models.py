class Livro:
    def __init__(self, nome, categoria, autor, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.autor = autor


class Usuario:
    def __init__(self, nome, nick, senha):
        self.nome = nome
        self.nick = nick
        self.senha = senha
