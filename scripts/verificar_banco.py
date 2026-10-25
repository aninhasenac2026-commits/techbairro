from pathlib import Path
import sqlite3

PASTA_DO_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_BANCO = PASTA_DO_PROJETO / "techbairro.db"

print(f"Banco verificado: {CAMINHO_BANCO}")
if not CAMINHO_BANCO.exists():
    print("O banco ainda não existe. Execute python techbairro.py para criá-lo.")
    raise SystemExit(0)

with sqlite3.connect(CAMINHO_BANCO) as conexao:
    tabelas = conexao.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()
    print("Tabelas:", ", ".join(item[0] for item in tabelas) or "(nenhuma)")
    try:
        total = conexao.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]
        print(f"Clientes cadastrados: {total}")
    except sqlite3.Error as erro:
        print(f"Não foi possível consultar a tabela clientes: {erro}")
