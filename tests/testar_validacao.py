import unittest
from cliente import Cliente
from validacao import ValidadorCliente


class TestesValidadorCliente(unittest.TestCase):
    def setUp(self):
        self.validador = ValidadorCliente()

    def cliente_valido(self):
        return Cliente("Ana Souza", "61999990001", "ana@email.com", "Rua 1 Casa 2")

    def test_cliente_valido(self):
        self.assertIsNone(self.validador.validar(self.cliente_valido()))

    def test_endereco_vazio(self):
        cliente = self.cliente_valido()
        cliente.endereco = ""
        self.assertEqual(self.validador.validar(cliente),
                         "Preencha o(s) campo(s): Endereço")

    def test_telefone_com_letras(self):
        cliente = self.cliente_valido()
        cliente.telefone = "6199ABC0001"
        self.assertEqual(self.validador.validar(cliente),
                         "Telefone inválido: use somente números.")

    def test_email_sem_ponto(self):
        cliente = self.cliente_valido()
        cliente.email = "ana@email"
        self.assertEqual(self.validador.validar(cliente),
                         "E-mail inválido: informe um endereço válido.")

    def test_nome_e_telefone_vazios(self):
        cliente = self.cliente_valido()
        cliente.nome = ""
        cliente.telefone = ""
        self.assertEqual(self.validador.validar(cliente),
                         "Preencha o(s) campo(s): Nome, Telefone")

    def test_email_sem_nome(self):
        self.assertFalse(self.validador.email_parece_valido("@email.com"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
