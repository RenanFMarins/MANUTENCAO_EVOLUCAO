class LoggerSingleton:
    _instance = None

    def __init__(self, nome_arquivo="app.log"):
        self.nome_arquivo = nome_arquivo
        print(f"[LoggerSingleton] Iniciado. Logando em: {self.nome_arquivo}")

    @classmethod
    def get_instance(cls, nome_arquivo="app.log"):
        if cls._instance is None:
            cls._instance = cls(nome_arquivo)
        return cls._instance

    def log(self, nivel, mensagem):
        with open(self.nome_arquivo, "a") as f:
            f.write(f"[{nivel.upper()}] {mensagem}\n")
