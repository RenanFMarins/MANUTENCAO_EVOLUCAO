from exercicio_009.logger_singleton import LoggerSingleton


class ModuloA:
    def __init__(self):
        self.logger = LoggerSingleton.get_instance()

    def fazer_algo_importante(self):
        self.logger.log("info", "Módulo A: Algo importante aconteceu.")
        self.logger.log("debug", "Módulo A: Detalhes do processamento.")
