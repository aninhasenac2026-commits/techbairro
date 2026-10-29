# Changelog da TechBairro

## v3.3.1 (Aulas 21–31)
### Adicionado
- Busca de clientes pelo nome.
- Testes automatizados para validação e operações do banco.
- README, manual de uso e instruções para publicação.
- Scripts para verificar o banco, importar CSV e gerar pacote.
### Alterado
- Separação do modelo, dados, validação e interface em módulos.
- A versão do aplicativo fica na constante `VERSAO`.
### Corrigido
- Consultas SQLite usam parâmetros para evitar montar SQL com texto digitado.
- Caminho do banco é calculado a partir da pasta do programa.

## v3.3.0 (Aula 20)
### Adicionado
- Cadastro, consulta, alteração e exclusão de clientes no SQLite.
- Busca por nome.

## v3.2.0 (Aula 16)
### Alterado
- Banco aberto pelo caminho completo relativo à pasta do projeto.
### Adicionado
- Mensagem "Banco em uso" no terminal.

## Preparação de entrega
### Adicionado
- Script `scripts/criar_banco.py` para criar/verificar o banco local sem abrir a interface.
- Instruções revisadas para execução, testes, criação do banco e geração do pacote ZIP.

## v3.2.1 (Aula 27)
### Adicionado
- README com requisitos, instalação e configuração do banco.
- Arquivo requirements.txt.
- Manual de uso em docs/manual_de_uso.md.
- Registro de testes em docs/registro_de_testes.md.