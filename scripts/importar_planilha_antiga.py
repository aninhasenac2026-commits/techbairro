"""Importa clientes de um CSV UTF-8 com cabeçalho Nome,Telefone,E-mail,Endereço.

Exemplo:
python scripts/importar_planilha_antiga.py caminho/para/clientes.csv
"""
import csv
import sys
from pathlib import Path

PASTA_DO_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PASTA_DO_PROJETO))

from banco import GerenciadorClientes
from cliente import Cliente
from validacao import ValidadorCliente

CAMINHO_BANCO = PASTA_DO_PROJETO / "techbairro.db"


def main():
    if len(sys.argv) != 2:
        print("Uso: python scripts/importar_planilha_antiga.py arquivo.csv")
        raise SystemExit(2)

    caminho_csv = Path(sys.argv[1])
    if not caminho_csv.is_file():
        print(f"Arquivo não encontrado: {caminho_csv}")
        raise SystemExit(2)

    banco = GerenciadorClientes(str(CAMINHO_BANCO))
    validador = ValidadorCliente()
    importados = recusados = 0

    with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        obrigatorias = {"Nome", "Telefone", "E-mail", "Endereço"}
        if not leitor.fieldnames or not obrigatorias.issubset(set(leitor.fieldnames)):
            print("O CSV precisa ter as colunas: Nome, Telefone, E-mail, Endereço")
            raise SystemExit(2)

        for numero_linha, linha in enumerate(leitor, start=2):
            cliente = Cliente(
                (linha.get("Nome") or "").strip(),
                (linha.get("Telefone") or "").strip(),
                (linha.get("E-mail") or "").strip(),
                (linha.get("Endereço") or "").strip(),
            )
            erro = validador.validar(cliente)
            if erro:
                print(f"Linha {numero_linha} ({cliente.nome or 'sem nome'}): recusada — {erro}")
                recusados += 1
                continue
            banco.cadastrar(cliente)
            importados += 1

    print(f"Importação concluída. Importados: {importados}. Recusados: {recusados}.")


if __name__ == "__main__":
    main()
