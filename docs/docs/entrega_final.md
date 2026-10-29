# Entrega final da TechBairro

**Aluno(a):** Aninha  
**Versão entregue:** 3.2.1

**Por que esse número de versão:** A versão 3.2.1 foi escolhida para registrar uma atualização do projeto com documentação e registro de testes, sem adicionar uma nova funcionalidade principal.

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os 6 casos de teste passaram | `docs/Registro_de_testes.md` — registro dos seis testes realizados. |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | Janela da aplicação mostrando `v3.2.1`; conferir `CHANGELOG.md` e `README.md`. |
| 3 | O pacote foi testado numa pasta limpa | Pacote ZIP extraído na Área de Trabalho; execução de `python techbairro.py`; janela mostrou `v3.2.1` e contador igual a 0. |
| 4 | Tag e release publicadas, com o .zip anexado | Tag `v3.2.1` enviada ao GitHub. Release e anexo ZIP: **confirmar** em https://github.com/aninhasenac2026-commits/techbairro/releases |
| 5 | O repositório não tem banco, __pycache__ nem dist | Conferir no repositório GitHub se `techbairro.db`, `__pycache__` e `dist` não aparecem. |
| 6 | O histórico tem commits com mensagens claras | https://github.com/aninhasenac2026-commits/techbairro/commits/main |
| 7 | README, manual de uso e requirements.txt estão no repositório | `README.md`, `docs/manual_de_uso.md` e `requirements.txt` — confirmar se os três estão publicados. |
| 8 | A Issue "Teste do README" (Aula 26) está fechada | Conferir a lista de Issues do repositório e confirmar que a Issue está fechada. |
| 9 | O vídeo está publicado e o link abre sem pedir login | **Preencher depois de publicar o vídeo:** inserir o link do vídeo. |

## Roteiro do vídeo

### 1. Problema e solução — 30 segundos
Apresentar a TechBairro 3.2.1 como um sistema de cadastro de clientes que permite cadastrar, consultar, editar e excluir registros, com validação dos dados.

### 2. Demonstração — 1 minuto e 30 segundos
Cadastrar um cliente, consultar os registros, editar o telefone, excluir um cliente com confirmação e demonstrar a validação de um telefone com espaços.

### 3. Como foi construída — 30 segundos
Explicar que o sistema utiliza Python e SQLite, possui arquivos separados para validação e acesso ao banco de dados, conta com testes e está versionado no GitHub.

### 4. Aprendizado — 30 segundos
Comentar a importância dos testes, da validação de dados e do controle de versões. Como melhoria futura, mencionar o aprimoramento da interface e a ampliação dos testes automatizados.

## Perguntas

**1. Por que o arquivo `techbairro.db` não deve ser enviado ao GitHub?**

Porque o banco de dados pode conter dados locais de teste e informações que não devem ser compartilhadas. O sistema deve conseguir criar ou utilizar um banco de dados local quando for executado.

**2. Qual teste encontrou um defeito real e qual foi o defeito?**

Preencher com o resultado real dos testes. Se nenhum defeito foi encontrado, informar que os testes não identificaram defeitos nessa execução.

**3. Como uma pessoa voluntária instala e executa o sistema a partir do repositório?**

A pessoa deve clonar ou baixar o repositório, instalar os requisitos listados em `requirements.txt`, seguir as instruções do README e executar `python techbairro.py` no terminal, dentro da pasta do projeto.

## Autoavaliação

Durante o desenvolvimento da TechBairro, pratiquei programação em Python, validação de dados, testes e utilização do SQLite. Também aprendi a registrar alterações com Git e publicar versões no GitHub. Como melhoria futura, pretendo aprimorar a interface e ampliar os testes automatizados.
