# logger_simples.py (simulando um logger básico)
class LoggerSimples:
    def __init__(self, nome_arquivo="app.log"):
        self.nome_arquivo = nome_arquivo
        print(f"[LoggerSimples] Iniciado. Logando em: {self.nome_arquivo}")

    def log(self, nivel, mensagem):
        with open(self.nome_arquivo, "a") as f:
            f.write(f"[{nivel.upper()}] {mensagem}\n")
