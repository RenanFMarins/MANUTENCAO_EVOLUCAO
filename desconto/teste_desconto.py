# test_desconto.py
import unittest
from desconto.core import calcular_desconto_cliente


class TestCalcularDescontoCliente(unittest.TestCase):
    def test_ouro_com_fidelidade(self):
        self.assertEqual(calcular_desconto_cliente('OURO', 250, 12), 0.20)

    def test_ouro_sem_fidelidade(self):
        self.assertEqual(calcular_desconto_cliente('OURO', 250, 5), 0.15)

    def test_ouro_valor_baixo(self):
        self.assertEqual(calcular_desconto_cliente('OURO', 180, 15), 0.10)

    def test_prata_valor_alto(self):
        self.assertEqual(calcular_desconto_cliente('PRATA', 200, 3), 0.10)

    def test_prata_valor_baixo(self):
        self.assertEqual(calcular_desconto_cliente('PRATA', 100, 0), 0.05)

    def test_bronze_valor_alto(self):
        self.assertEqual(calcular_desconto_cliente('BRONZE', 120, 0), 0.05)

    def test_bronze_valor_baixo(self):
        self.assertEqual(calcular_desconto_cliente('BRONZE', 80, 0), 0.0)

    def test_novo_cliente_sem_desconto(self):
        self.assertEqual(calcular_desconto_cliente('NOVO', 90, 0), 0.0)

    def test_novo_cliente_com_desconto(self):
        self.assertEqual(calcular_desconto_cliente('NOVO', 150, 0), 0.05)


if __name__ == '__main__':
    unittest.main()
