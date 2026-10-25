# Manual de uso da TechBairro

## A tela principal
A janela mostra os campos **Nome**, **Telefone**, **E-mail** e **Endereço**. Os botões são **Salvar**, **Cancelar/Limpar** e **Consultar clientes**. A mensagem de situação e o contador mostram o resultado das ações e a quantidade de clientes cadastrados.

## Cadastrar um cliente
1. Preencha Nome, Telefone, E-mail e Endereço.
2. Digite o telefone somente com números.
3. Clique em **Salvar**.
4. Se aparecer um aviso, corrija o campo indicado.
5. Confirme a mensagem de sucesso.

## Consultar e buscar
1. Clique em **Consultar clientes**.
2. Para buscar, digite parte do nome e clique em **Buscar**.
3. Para voltar à lista completa, clique em **Mostrar todos**.
4. Clique em **Atualizar lista** para carregar os dados novamente.

## Alterar um cadastro
1. Na consulta, selecione o cliente.
2. Clique em **Editar selecionado** ou dê dois cliques no nome.
3. Altere os campos na janela principal.
4. Clique em **Salvar edição**.
5. Para desistir, clique em **Cancelar/Limpar**.

## Excluir um cadastro
1. Na consulta, selecione o cliente.
2. Clique em **Excluir selecionado**.
3. Confira os dados e confirme somente se selecionou a pessoa correta.
4. A lista e o contador serão atualizados.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Não deixe vazio. |
| Telefone | Sim | Use somente números, sem espaços ou símbolos. |
| E-mail | Sim | Deve ter nome, `@` e domínio com ponto, por exemplo `ana@email.com`. |
| Endereço | Sim | Não deixe vazio. |

## Mensagens comuns

| Mensagem | O que significa | O que fazer |
|---|---|---|
| `Formulário pronto` | O programa está pronto. | Comece a preencher. |
| `Cliente 'NOME' cadastrado com sucesso!` | O cadastro foi salvo. | Confira o contador. |
| `Cliente 'NOME' atualizado com sucesso!` | As alterações foram salvas. | Continue usando. |
| `Cliente 'NOME' excluído com sucesso!` | O cadastro foi removido. | Confira a lista. |
| `Preencha o(s) campo(s): ...` | Há campos vazios. | Preencha os campos indicados. |
| `Telefone inválido: use somente números.` | O telefone contém caracteres não numéricos. | Digite somente números. |
| `E-mail inválido: informe um endereço válido.` | O e-mail está incompleto ou fora do formato esperado. | Confira o nome, o `@` e o domínio. |
| `Selecione um cliente antes de editar.` | Nenhuma linha foi selecionada para edição. | Selecione um cliente. |
| `Selecione um cliente antes de excluir.` | Nenhuma linha foi selecionada para exclusão. | Selecione um cliente. |

## Dúvidas frequentes

**O que faço se aparecer uma mensagem de campo vazio?**  
Preencha todos os campos indicados e clique em Salvar novamente.

**Posso usar traço ou espaço no telefone?**  
Não. Digite somente números.

**Onde ficam os cadastros?**  
No arquivo `techbairro.db`, na pasta do projeto. Não apague esse arquivo se quiser manter os dados.

**Como faço uma cópia de segurança?**  
Feche o programa e copie `techbairro.db` para uma pasta segura. Não publique esse arquivo na internet.

**A exclusão pode ser desfeita?**  
Não pelo aplicativo. Leia a confirmação com atenção antes de escolher Sim.
