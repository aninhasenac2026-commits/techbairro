# Modelo: representa os dados de um cliente.
# Este arquivo não depende da tela nem do banco de dados.

class Cliente:
    def __init__(self, nome, telefone, email, endereco, cliente_id=None):
        self.id = cliente_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email}"
