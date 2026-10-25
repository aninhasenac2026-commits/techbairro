# Camada de dados: toda a comunicação com SQLite fica neste arquivo.

import sqlite3
from cliente import Cliente


class GerenciadorClientes:
    def __init__(self, caminho_banco):
        self.caminho_banco = caminho_banco
        self.criar_tabela()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela(self):
        with self.conectar() as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    endereco TEXT NOT NULL
                )
            """)

    def cadastrar(self, cliente):
        with self.conectar() as conexao:
            cursor = conexao.execute("""
                INSERT INTO clientes (nome, telefone, email, endereco)
                VALUES (?, ?, ?, ?)
            """, (cliente.nome, cliente.telefone, cliente.email, cliente.endereco))
            return cursor.lastrowid

    def listar(self):
        with self.conectar() as conexao:
            linhas = conexao.execute("""
                SELECT id, nome, telefone, email, endereco
                FROM clientes
                ORDER BY nome COLLATE NOCASE, id
            """).fetchall()
        return [Cliente(nome, telefone, email, endereco, cliente_id)
                for cliente_id, nome, telefone, email, endereco in linhas]

    def buscar_por_nome(self, texto):
        termo = f"%{texto.strip()}%"
        with self.conectar() as conexao:
            linhas = conexao.execute("""
                SELECT id, nome, telefone, email, endereco
                FROM clientes
                WHERE nome LIKE ?
                ORDER BY nome COLLATE NOCASE, id
            """, (termo,)).fetchall()
        return [Cliente(nome, telefone, email, endereco, cliente_id)
                for cliente_id, nome, telefone, email, endereco in linhas]

    def atualizar(self, cliente_id, cliente):
        with self.conectar() as conexao:
            cursor = conexao.execute("""
                UPDATE clientes
                SET nome = ?, telefone = ?, email = ?, endereco = ?
                WHERE id = ?
            """, (cliente.nome, cliente.telefone, cliente.email,
                  cliente.endereco, cliente_id))
            return cursor.rowcount > 0

    def remover(self, cliente_id):
        with self.conectar() as conexao:
            cursor = conexao.execute(
                "DELETE FROM clientes WHERE id = ?", (cliente_id,)
            )
            return cursor.rowcount > 0

    def total(self):
        with self.conectar() as conexao:
            return conexao.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]
