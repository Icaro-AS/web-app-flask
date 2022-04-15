class Livro:
    def __init__(self, nome, categoria, autor, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.autor = autor


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
