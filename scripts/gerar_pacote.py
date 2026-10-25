"""Gera um ZIP limpo da versão informada em techbairro.py."""
from pathlib import Path
import re
import zipfile

RAIZ = Path(__file__).resolve().parent.parent
CODIGO = (RAIZ / "techbairro.py").read_text(encoding="utf-8")
CHANGELOG = (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8")
match = re.search(r"^VERSAO\s*=\s*['\"]([^'\"]+)['\"]", CODIGO, re.M)
if not match:
    raise SystemExit("Erro: não encontrei a constante VERSAO no techbairro.py.")
versao = match.group(1)
if f"## v{versao}" not in CHANGELOG:
    raise SystemExit(f"Erro: registre a versão {versao} no CHANGELOG.md antes de empacotar.")

destino = RAIZ / "dist" / f"TechBairro-{versao}.zip"
destino.parent.mkdir(exist_ok=True)
excluir_partes = {".git", ".venv", "venv", "__pycache__", "dist", "build"}
excluir_nomes = {"techbairro.db", "Thumbs.db", ".DS_Store"}
with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as pacote:
    for caminho in RAIZ.rglob("*"):
        if not caminho.is_file() or caminho == destino:
            continue
        relativo = caminho.relative_to(RAIZ)
        if any(parte in excluir_partes for parte in relativo.parts):
            continue
        if caminho.name in excluir_nomes or caminho.suffix in {".pyc", ".pyo"}:
            continue
        pacote.write(caminho, relativo.as_posix())
print(f"Pacote criado: {destino}")
