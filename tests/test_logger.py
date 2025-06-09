import os
import unittest
from exercicio_009.logger_singleton import LoggerSingleton
from exercicio_009.modulo_a import ModuloA
from exercicio_009.modulo_b import ModuloB

LOG_FILE = "test_log.log"


class TestLoggerSingleton(unittest.TestCase):

    def setUp(self):
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)

    def tearDown(self):
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)

    def test_singleton_instance(self):
        logger1 = LoggerSingleton.get_instance(LOG_FILE)
        logger2 = LoggerSingleton.get_instance("outro_nome.log")
        self.assertIs(logger1, logger2)
        self.assertEqual(logger1.nome_arquivo, LOG_FILE)

    def test_logger_writes_to_file(self):
        logger = LoggerSingleton.get_instance(LOG_FILE)
        logger.log("info", "Mensagem de teste")
        with open(LOG_FILE, "r") as f:
            content = f.read()
        self.assertIn("Mensagem de teste", content)
        self.assertIn("[INFO]", content)

    def test_modulo_a_usa_logger_singleton(self):
        modulo_a = ModuloA()
        modulo_a.fazer_algo_importante()
        with open(LOG_FILE, "r") as f:
            content = f.read()
        self.assertIn("Módulo A: Algo importante aconteceu.", content)
        self.assertIn("Módulo A: Detalhes do processamento.", content)

    def test_modulo_b_usa_logger_singleton_e_loga_erro(self):
        modulo_b = ModuloB()
        modulo_b.outra_tarefa()
        with open(LOG_FILE, "r") as f:
            content = f.read()
        self.assertIn("Módulo B: Outra tarefa executada.", content)
        self.assertIn("Módulo B: Tentativa de divisão por zero!", content)


if __name__ == "__main__":
    unittest.main()
