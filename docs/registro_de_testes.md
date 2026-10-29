# Registro de testes da TechBairro

**Versão testada:** A preencher após conferir a versão final  
**Data:** A preencher no dia dos testes  
**Responsável:** A preencher  
**Sistema operacional e versão do Python:** A preencher

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
CT01	RF01	Cadastrar Ana Silva com todos os campos corretos.	O cliente deve ser cadastrado com sucesso e aparecer na consulta.	Cliente 'Ana Silva' cadastrado com sucesso! Contador: Clientes cadastrados: 2.	Aprovado
ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT02	RF01	Tentar salvar com Nome e Endereço vazios.	O sistema deve impedir o cadastro e informar os campos obrigatórios.	Preencha o(s) campo(s): Nome, Endereço	Aprovado
ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT03	RF02	Informar o telefone 61 9999 0000, com espaços.	O sistema deve rejeitar o telefone e exibir a mensagem de validação.	Telefone inválido: use somente números.	Aprovado
ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT04	RF03	Informar o e-mail ana@email, sem ponto no domínio.	O sistema deve rejeitar o e-mail e exibir a mensagem de validação.	E-mail inválido: informe um endereço válido.	Aprovado
ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT05	RF05	Editar Ana Silva e trocar o telefone para 61988887777.	O sistema deve salvar a alteração e apresentar o telefone atualizado.	Cliente 'Ana Silva' atualizado com sucesso!	Aprovado, após confirmar o telefone atualizado.
ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT06	RF06	Tentar excluir James; responder Não e depois Sim.	Ao responder Não, o cliente deve permanecer. Ao responder Sim, deve ser excluído.	Ao clicar em Não, James permaneceu cadastrado. Ao clicar em Sim, apareceu Cliente 'James' excluído com sucesso!. Contador: Clientes cadastrados: 1.	Aprovado
## Testes automáticos

**Comando executado:** `python testar_validacao.py`

**Saída:** A preencher após executar o comando.

## Defeitos encontrados

A preencher após a execução dos testes. Registrar os defeitos reais, como foram corrigidos e o commit correspondente. Se nenhum defeito for encontrado, registrar "nenhum".
