# Registro de testes da TechBairro

**Versão testada:** A preencher após conferir a versão final  
**Data:** A preencher no dia dos testes  
**Responsável:** A preencher  
**Sistema operacional e versão do Python:** A preencher

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos corretos. | O cliente deve ser cadastrado com sucesso e aparecer na consulta. | A preencher após executar o teste. | Pendente |
| CT02 | RF01 | Tentar salvar com Nome e Endereço vazios. | O sistema deve impedir o cadastro e informar os campos obrigatórios. | A preencher após executar o teste. | Pendente |
| CT03 | RF02 | Informar o telefone `61 9999 0000`, com espaços. | O sistema deve rejeitar o telefone e exibir a mensagem de validação. | A preencher após executar o teste. | Pendente |
| CT04 | RF03 | Informar o e-mail `ana@email`, sem ponto no domínio. | O sistema deve rejeitar o e-mail e exibir a mensagem de validação. | A preencher após executar o teste. | Pendente |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar. | O sistema deve salvar a alteração e apresentar o telefone atualizado. | A preencher após executar o teste. | Pendente |
| CT06 | RF06 | Tentar excluir um cliente; responder Não e depois Sim. | Ao responder Não, o cliente deve permanecer. Ao responder Sim, deve ser excluído. | A preencher após executar o teste. | Pendente |

## Testes automáticos

**Comando executado:** `python testar_validacao.py`

**Saída:** A preencher após executar o comando.

## Defeitos encontrados

A preencher após a execução dos testes. Registrar os defeitos reais, como foram corrigidos e o commit correspondente. Se nenhum defeito for encontrado, registrar "nenhum".
