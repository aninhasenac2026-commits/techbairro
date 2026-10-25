import tempfile
import unittest
from pathlib import Path

from banco import GerenciadorClientes
from cliente import Cliente


class TestesBanco(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "teste.db")
        self.banco = GerenciadorClientes(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_cadastrar_listar_total(self):
        self.banco.cadastrar(Cliente("Bia Costa", "61977770000", "bia@email.com", "Rua 4"))
        self.assertEqual(self.banco.total(), 1)
        self.assertEqual(self.banco.listar()[0].nome, "Bia Costa")

    def test_buscar_por_nome(self):
        self.banco.cadastrar(Cliente("Bia Costa", "61977770000", "bia@email.com", "Rua 4"))
        self.banco.cadastrar(Cliente("Ana Souza", "61999990001", "ana@email.com", "Rua 1"))
        self.assertEqual([c.nome for c in self.banco.buscar_por_nome("bia")], ["Bia Costa"])

    def test_atualizar(self):
        cliente_id = self.banco.cadastrar(
            Cliente("Bia Costa", "61977770000", "bia@email.com", "Rua 4"))
        self.assertTrue(self.banco.atualizar(
            cliente_id, Cliente("Bia Costa", "61911110000", "bia@email.com", "Rua 4")))
        self.assertEqual(self.banco.listar()[0].telefone, "61911110000")

    def test_remover(self):
        cliente_id = self.banco.cadastrar(
            Cliente("Bia Costa", "61977770000", "bia@email.com", "Rua 4"))
        self.assertTrue(self.banco.remover(cliente_id))
        self.assertEqual(self.banco.total(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
