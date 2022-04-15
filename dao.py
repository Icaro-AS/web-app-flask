from models import Livro, Usuario

SQL_DELETA_LIVRO = 'delete from livro where id = %s'
SQL_LIVRO_POR_ID = 'SELECT id, nome, categoria, autor from livro where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_LIVRO = 'UPDATE livro SET nome=%s, categoria=%s, autor=%s where id = %s'
SQL_BUSCA_LIVROS = 'SELECT id, nome, categoria, autor from livro'
SQL_CRIA_LIVRO = 'INSERT into livro (nome, categoria, autor) values (%s, %s, %s)'


class LivroDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, livro):
        cursor = self.__db.connection.cursor()

        if (livro.id):
            cursor.execute(SQL_ATUALIZA_LIVRO, (livro.nome, livro.categoria, livro.autor, livro.id))
        else:
            cursor.execute(SQL_CRIA_LIVRO, (livro.nome, livro.categoria, livro.autor))
            livro.id = cursor.lastrowid
        self.__db.connection.commit()
        return livro

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LIVROS)
        livros = traduz_livros(cursor.fetchall())
        return livros

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LIVRO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Livro(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_LIVRO, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_livros(livros):
    def cria_livro_com_tupla(tupla):
        return Livro(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_livro_com_tupla, livros))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
