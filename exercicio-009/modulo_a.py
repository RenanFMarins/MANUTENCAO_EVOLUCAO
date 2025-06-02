# modulo_a.py
# from logger_simples import LoggerSimples # Supondo que está no mesmo diretório ou PYTHONPATH
class ModuloA:
    def __init__(self):
        self.logger = LoggerSimples("modulo_a.log") # Instância própria

    def fazer_algo_importante(self):
        self.logger.log("info", "Módulo A: Algo importante aconteceu.")
        self.logger.log("debug", "Módulo A: Detalhes do processamento.")
