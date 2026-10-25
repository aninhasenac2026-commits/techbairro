"""Verifica se o banco pode ser aberto para leitura e escrita."""
from pathlib import Path
import sqlite3

PASTA_DO_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_BANCO = PASTA_DO_PROJETO / "techbairro.db"

print(f"Banco verificado: {CAMINHO_BANCO}")
try:
    with sqlite3.connect(CAMINHO_BANCO, timeout=2) as conexao:
        conexao.execute("BEGIN IMMEDIATE")
        conexao.rollback()
    print("O banco pode ser aberto e está disponível.")
except sqlite3.Error as erro:
    print(f"Não foi possível acessar o banco: {erro}")
    raise SystemExit(1)
