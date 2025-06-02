# modulo_b.py
# from logger_simples import LoggerSimples
class ModuloB:
    def __init__(self):
        self.logger = LoggerSimples("modulo_b.log") # Outra instância própria

    def outra_tarefa(self):
        self.logger.log("info", "Módulo B: Outra tarefa executada.")
        try:
            x = 1 / 0
        except ZeroDivisionError:
            self.logger.log("error", "Módulo B: Tentativa de divisão por zero!")
