# Regras de negócio: valida os dados sem abrir a tela ou acessar o banco.

class ValidadorCliente:
    def validar(self, cliente):
        vazios = []
        if not cliente.nome.strip():
            vazios.append("Nome")
        if not cliente.telefone.strip():
            vazios.append("Telefone")
        if not cliente.email.strip():
            vazios.append("E-mail")
        if not cliente.endereco.strip():
            vazios.append("Endereço")

        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido: informe um endereço válido."

        return None

    def email_parece_valido(self, email):
        if email.count("@") != 1:
            return False
        nome, dominio = email.split("@")
        if not nome or not dominio or "." not in dominio:
            return False
        partes = dominio.split(".")
        if any(not parte for parte in partes):
            return False
        return True
