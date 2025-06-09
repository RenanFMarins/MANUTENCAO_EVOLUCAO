from exercicio_009.logger_singleton import LoggerSingleton
from exercicio_009.modulo_a import ModuloA
from exercicio_009.modulo_b import ModuloB

if __name__ == "__main__":
    print("-- Executando sem Singleton --")
    servico_a = ModuloA()
    servico_a.fazer_algo_importante()

    servico_b = ModuloB()
    servico_b.outra_tarefa()

    print("Verifique os arquivos modulo_a.log e modulo_b.log\n")


if __name__ == "__main__":
    print("--- Executando com Singleton ---")

    logger_global = LoggerSingleton.get_instance("app_global.log")
    logger_global.log("system", "Logger Singleton inicializado.")

    servico_a = ModuloA()
    servico_a.fazer_algo_importante()

    servico_b = ModuloB()
    servico_b.outra_tarefa()

    logger_a = servico_a.logger
    logger_b = servico_b.logger

    print(f"\nLogger A é o mesmo que Logger B? {'Sim' if logger_a is logger_b else 'Não'}")
    print("(Todos os logs devem estar em 'app_global.log')")
