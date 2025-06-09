import unittest
from frete.enums import MetodoEnvio
from frete.calculadora import CalculadoraFrete


class TestCalculadoraFrete(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraFrete()

    def test_frete_normal(self):
        custo = self.calc.calcular(MetodoEnvio.NORMAL, 2.0, 100.0)
        esperado = 5.0 + (2.0 * 1.5) + (100.0 * 0.10)
        self.assertAlmostEqual(custo, esperado, places=2)

    def test_frete_expresso(self):
        custo = self.calc.calcular(MetodoEnvio.EXPRESSO, 2.0, 100.0)
        esperado = 5.0 * 1.5 + (2.0 * 2.0) + (100.0 * 0.15)
        self.assertAlmostEqual(custo, esperado, places=2)

    def test_frete_sedex10(self):
        custo = self.calc.calcular(MetodoEnvio.SEDEX_10, 2.0, 100.0)
        esperado = 5.0 * 2.0 + (2.0 * 2.5) + (100.0 * 0.20) + 10.0
        self.assertAlmostEqual(custo, esperado, places=2)

    def test_frete_retirada(self):
        custo = self.calc.calcular(MetodoEnvio.RETIRADA, 2.0, 100.0)
        self.assertEqual(custo, 0.0)

    def test_frete_metodo_desconhecido(self):
        class MetodoFake:
            pass
        custo = self.calc.calcular(MetodoFake(), 2.0, 100.0)
        self.assertEqual(custo, 0.0)

if __name__ == "__main__":
    unittest.main()
