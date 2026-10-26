# TechBairro

Aplicativo desktop em Python para a associação de moradores cadastrar, consultar, alterar, buscar e excluir clientes. A interface usa Tkinter e os dados ficam em um banco SQLite local.

**Versão:** 3.3.1 · Veja o [histórico de mudanças](CHANGELOG.md).

## Funcionalidades
- Cadastro de clientes com nome, telefone, e-mail e endereço.
- Validação dos campos obrigatórios, telefone numérico e formato básico de e-mail.
- Consulta de clientes, busca por nome, edição e exclusão com confirmação.
- Persistência em SQLite: os dados continuam disponíveis após fechar o aplicativo.

## Requisitos
- Python 3.10 ou superior recomendado.
- Tkinter disponível na instalação do Python.
- Nenhuma biblioteca externa.
- Internet somente para baixar o repositório; não é necessária para o uso normal.

## Instalação

### Opção 1 — Git
Instale o Python e o Git. No terminal, execute:

```bash
git clone https://github.com/SEU-USUARIO/TechBairro.git
cd TechBairro
python --version
python -m tkinter
python -m pip install -r requirements.txt
python techbairro.py
```

### Opção 2 — baixar ZIP
No GitHub, clique em **Code → Download ZIP**, extraia o arquivo, abra um terminal na pasta extraída e execute:

```bash
python --version
python -m tkinter
python -m pip install -r requirements.txt
python techbairro.py
```

`python -m tkinter` deve abrir uma pequena janela de teste. Feche-a antes de iniciar o programa. `pip install -r requirements.txt` não instala pacotes externos porque o projeto usa apenas a biblioteca padrão.

Ao iniciar, o terminal mostra `Banco em uso: ...` e abre a janela do cadastro.

## Como usar
Consulte o [manual de uso](docs/manual_de_uso.md).

## Banco de dados e privacidade
O arquivo `techbairro.db` é criado automaticamente na pasta do projeto. Ele pode conter dados pessoais; por isso está no `.gitignore` e não deve ser enviado ao GitHub. Para fazer backup, feche o aplicativo e copie esse arquivo para um local seguro com acesso restrito.

## Estrutura

```text
TechBairro/
├── techbairro.py
├── cliente.py
├── banco.py
├── validacao.py
├── requirements.txt
├── CHANGELOG.md
├── README.md
├── COMO_EXECUTAR.txt
├── .gitignore
├── docs/
│   └── manual_de_uso.md
├── scripts/
│   ├── gerar_pacote.py
│   ├── verificar_banco.py
│   ├── travar_banco.py
│   └── importar_planilha_antiga.py
└── tests/
    ├── testar_validacao.py
    └── testar_banco.py
```

## Testes

```bash
python -m unittest discover -s tests -v
```

## Autor
Ana Carolina — Técnico em Desenvolvimento de Sistemas, Senac DF.
