# Registro de testes da TechBairro

**Versão testada:** preencher após conferir a constante `VERSAO` em `techbairro.py`  
**Data:** preencher com a data em que os testes forem executados  
**Responsável:** preencher com seu nome  
**Sistema operacional:** preencher com o nome e a versão do sistema usado  
**Versão do Python:** preencher com o resultado de `python --version` (ou `python3 --version`, se esse for o comando que funcionar)

> **Importante:** os resultados obtidos e os status ainda não foram preenchidos, porque os testes precisam ser executados no programa. Não marque um teste como aprovado antes de conferir o resultado real. Use somente dados fictícios.

## Casos de teste

| ID | Requisito | Passos e dados | Resultado esperado (definido antes do teste) | Resultado obtido (preencher depois) | Status |
|---|---|---|---|---|---|
| CT01 | RF01 — Cadastro | Preencher todos os campos com dados válidos e clicar em **Salvar**. Exemplo fictício: Ana Souza; `61999990001`; `ana@email.com`; `Rua 10`. | O cliente deve ser cadastrado. A tela deve mostrar uma mensagem de sucesso, o contador deve aumentar em 1 e os campos devem ser limpos. Confira no código/tela qual é a mensagem exata esperada. | **PREENCHER APÓS EXECUTAR:** registrar a mensagem exata da tela, o que aconteceu com o contador e os campos. | Pendente |
| CT02 | RF01 — Campos obrigatórios | Deixar **Nome** e **Endereço** vazios; preencher os outros campos com dados válidos e clicar em **Salvar**. Exemplo: Nome vazio; `61999990002`; `b@email.com`; Endereço vazio. | O sistema deve impedir o cadastro e indicar que Nome e Endereço são obrigatórios. Nenhum cliente deve ser cadastrado e o contador não deve aumentar. | **PREENCHER APÓS EXECUTAR:** copiar a mensagem exata da tela e confirmar se nenhum cliente foi cadastrado. | Pendente |
| CT03 | RF02 — Validação do telefone | Preencher os campos com dados fictícios válidos, mas usar o telefone `61 9999 0000` (com espaços); clicar em **Salvar**. | O sistema deve rejeitar o telefone com espaços, informar que o telefone deve conter somente números e não cadastrar o cliente. | **PREENCHER APÓS EXECUTAR:** copiar a mensagem exata da tela e confirmar se o cadastro foi bloqueado. | Pendente |
| CT04 | RF03 — Validação do e-mail | Preencher os campos com dados fictícios, usando `ana@email` como e-mail (sem ponto após o `@`); clicar em **Salvar**. | O sistema deve rejeitar o e-mail sem domínio válido e não cadastrar o cliente. | **PREENCHER APÓS EXECUTAR:** copiar a mensagem exata da tela e confirmar se o cadastro foi bloqueado. | Pendente |
| CT05 | RF05 — Edição | Cadastrar ou localizar um cliente fictício, abrir a edição, trocar o telefone por outro número válido e salvar. Depois, abrir a Consulta novamente e conferir os dados. | O sistema deve salvar a alteração, mostrar uma mensagem de sucesso e exibir o telefone novo na Consulta. Os outros dados do cliente devem permanecer corretos. | **PREENCHER APÓS EXECUTAR:** registrar a mensagem exata e o telefone que aparece na Consulta após reabri-la. | Pendente |
| CT06 | RF06 — Exclusão com confirmação | Selecionar um cliente fictício para excluir. Na confirmação, responder **Não** e verificar que ele continua na lista. Repetir a exclusão do mesmo cliente e responder **Sim**; conferir a lista e o contador. | Ao responder **Não**, o cliente deve continuar cadastrado. Ao responder **Sim**, o cliente deve ser excluído e a lista/contador devem ser atualizados corretamente. | **PREENCHER APÓS EXECUTAR:** registrar o que aconteceu nas duas respostas e quaisquer mensagens exibidas. | Pendente |

## Testes automáticos

Execute o comando abaixo no terminal, dentro da pasta do projeto:

```bash
python testar_validacao.py
```

Se o comando `python` não funcionar, tente:

```bash
python3 testar_validacao.py
```

**Saída do teste automático:**  
PREENCHER AQUI com a saída real exibida no terminal. Não escreva “passou” sem executar o comando.

## Defeitos encontrados

**Situação inicial:** testes ainda não executados; não é possível afirmar se foram encontrados defeitos.

Depois de executar os casos, registre aqui:
- **Caso de teste:** qual CT apresentou problema.
- **O que aconteceu:** mensagem ou comportamento real observado.
- **O que era esperado:** comportamento descrito na tabela.
- **Correção aplicada:** o que foi alterado, se houver.
- **Commit:** identificador ou mensagem do commit que contém a correção, se houver.
- **Reteste:** resultado após executar novamente o teste.

Se todos os testes forem executados e nenhum defeito for encontrado, escreva **“Nenhum defeito encontrado nos testes executados”**. Se algum teste falhar, registre o problema e repita o teste após a correção.

## Como descobrir as informações do ambiente

1. Abra a pasta do projeto no VS Code.
2. Abra o terminal: **Terminal → Novo Terminal**.
3. Para descobrir a versão do Python, execute `python --version`. Se não funcionar, tente `python3 --version`.
4. Anote o sistema operacional e sua versão nas informações do início deste documento.
5. Confira a constante `VERSAO` no arquivo `techbairro.py` para registrar a versão que realmente será testada.
6. Execute os seis casos no programa e preencha **Resultado obtido** e **Status** com o que realmente aconteceu.

**Status sugeridos:** `Aprovado`, `Reprovado` ou `Pendente`.
