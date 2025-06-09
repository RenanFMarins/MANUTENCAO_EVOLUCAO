import unittest
from io import StringIO
import sys
from produto.exercicio_006 import Produto


class TestProduto(unittest.TestCase):

    def test_criacao_valida(self):
        p = Produto("Lápis", 2.5, 50)
        self.assertEqual(p.get_nome(), "Lápis")
        self.assertEqual(p.get_preco(), 2.5)
        self.assertEqual(p.get_estoque(), 50)

    def test_preco_negativo(self):
        p = Produto("Borracha", 1.0, 30)
        p.set_preco(-10)
        self.assertEqual(p.get_preco(), 1.0)

    def test_estoque_negativo(self):
        p = Produto("Caderno", 10.0, 100)
        p.set_estoque(-20)
        self.assertEqual(p.get_estoque(), 100)

    def test_modificacao_valida(self):
        p = Produto("Caneta", 1.5, 20)
        p.set_preco(2.0)
        p.set_estoque(30)
        self.assertEqual(p.get_preco(), 2.0)
        self.assertEqual(p.get_estoque(), 30)

    def test_exibir_detalhes(self):
        p = Produto("Marca Texto", 3.5, 40)
        captured_output = StringIO()
        sys.stdout = captured_output
        p.exibir_detalhes()
        sys.stdout = sys.__stdout__
        self.assertIn("Produto: Marca Texto", captured_output.getvalue())
        self.assertIn("Preço: R$3.50", captured_output.getvalue())
        self.assertIn("Estoque: 40", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
