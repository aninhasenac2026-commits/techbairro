"""Cria o banco local do TechBairro e a tabela de clientes, se necessário."""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))
from banco import GerenciadorClientes  # noqa: E402

CAMINHO_BANCO = RAIZ / "techbairro.db"
GerenciadorClientes(str(CAMINHO_BANCO))
print(f"Banco criado/verificado: {CAMINHO_BANCO}")
print("A tabela clientes está pronta. Nenhum cliente foi adicionado.")
