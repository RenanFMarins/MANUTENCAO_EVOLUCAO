from exercicio_009.logger_singleton import LoggerSingleton


class ModuloB:
    def __init__(self):
        self.logger = LoggerSingleton.get_instance()

    def outra_tarefa(self):
        self.logger.log("info", "Módulo B: Outra tarefa executada.")
        try:
            x = 1 / 0
        except ZeroDivisionError:
            self.logger.log("error", "Módulo B: Tentativa de divisão por zero!")
