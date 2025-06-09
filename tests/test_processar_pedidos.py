import unittest
from exercicio_008 import processar_pedidos_por_categoria


class TestProcessarPedidos(unittest.TestCase):

    def setUp(self):
        self.lista_pedidos = [
            {
                "id": "P001",
                "itens": [
                    {"nome_produto": "Laptop Gamer", "categoria": "Eletrônicos", "preco": 7500.00},
                    {"nome_produto": "Mouse Sem Fio", "categoria": "Acessórios", "preco": 150.00}
                ]
            },
            {
                "id": "P002",
                "itens": [
                    {"nome_produto": "Teclado Mecânico", "categoria": "Acessórios", "preco": 450.00},
                    {"nome_produto": "Monitor Ultrawide", "categoria": "Eletrônicos", "preco": 2200.00},
                    {"nome_produto": "SSD 1TB", "categoria": "Eletrônicos", "preco": 600.00}
                ]
            }
        ]

    def test_categoria_eletronicos(self):
        produtos, total = processar_pedidos_por_categoria(self.lista_pedidos, "Eletrônicos")
        self.assertEqual(produtos, ["Laptop Gamer", "Monitor Ultrawide", "SSD 1TB"])
        self.assertEqual(total, 7500.00 + 2200.00 + 600.00)

    def test_categoria_acessorios(self):
        produtos, total = processar_pedidos_por_categoria(self.lista_pedidos, "Acessórios")
        self.assertEqual(produtos, ["Mouse Sem Fio", "Teclado Mecânico"])
        self.assertEqual(total, 150.00 + 450.00)

    def test_categoria_inexistente(self):
        produtos, total = processar_pedidos_por_categoria(self.lista_pedidos, "Livros")
        self.assertEqual(produtos, [])
        self.assertEqual(total, 0)


if __name__ == '__main__':
    unittest.main()
