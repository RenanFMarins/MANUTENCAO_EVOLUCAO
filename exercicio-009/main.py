# main.py
# from modulo_a import ModuloA
# from modulo_b import ModuloB
if __name__ == "__main__":
    print("-- Executando sem Singleton --")
    servico_a = ModuloA()
    servico_a.fazer_algo_importante()

    servico_b = ModuloB()
    servico_b.outra_tarefa()

    print("Verifique os arquivos modulo_a.log e modulo_b.log\n")
