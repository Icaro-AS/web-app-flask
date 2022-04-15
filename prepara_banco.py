import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="Aleteia7*",
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()

cursor.execute('create database if not exists livraria')
cursor.execute('use livraria')
cursor.execute("""create table if not exists livro(
                id int(11) not null auto_increment,
                nome varchar(50) collate utf8_bin not null,
                categoria varchar(40) collate utf8_bin not null,
                autor varchar(50) not null,
                primary key (id)
                )engine=innodb default charset=utf8 collate=utf8_bin"""
               )
cursor.execute("""create table if not exists usuario (
                id varchar(20) primary key not null,
                nome varchar(20) not null,
                senha varchar(20) not null
                )"""
               )

# inserindo usuarios
cursor.executemany(
      'INSERT INTO livraria.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('Batman', 'morcego', 'batmanwayne'),
            ('Robin', 'Prodígio', 'garotobom'),
            ('Batgirl', 'gatinha', 'amobatman')
      ])

cursor.execute('select * from livraria.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
      'INSERT INTO livraria.livro (nome, categoria, autor) VALUES (%s, %s, %s)',
      [
            ('O senhor dos anéis', 'Fantasia', 'J.R.R Tolkien'),
            ('Cristianismo Puro e Simples', 'Filosofia', 'C.S Lewis'),
            ('Ortodoxia', 'Filosofia', 'G.K Chesterton')
      ])

cursor.execute('select * from livraria.livro')
print(' -------------  Jogos:  -------------')
for livro in cursor.fetchall():
    print(livro[1])

# commitando senão nada tem efeito
conexao.commit()
conexao.close()
