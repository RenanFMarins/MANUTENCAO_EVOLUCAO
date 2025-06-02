# Códigos de status (poderiam estar no topo do módulo ou dentro da classe)
# STATUS_PENDENTE = 0 (Exemplo de como seria antes da refatoração na classe)
# STATUS_PROCESSANDO = 1
# STATUS_ENVIADO = 2
# STATUS_ENTREGUE = 3
# STATUS_CANCELADO = 4

class Pedido:
    # Definindo como constantes de classe para melhor organização
    STATUS_PENDENTE = 0
    STATUS_PROCESSANDO = 1
    STATUS_ENVIADO = 2
    STATUS_ENTREGUE = 3
    STATUS_CANCELADO = 4  # Novo status adicionado sem constante explícita no exemplo original

    def __init__(self, status_codigo):
        self.status_codigo = status_codigo

    def get_status_descricao(self):
        if self.status_codigo == 0:  # Número mágico
            return "Pendente"
        elif self.status_codigo == 1:  # Número mágico
            return "Processando"
        elif self.status_codigo == 2:  # Número mágico
            return "Enviado"
        elif self.status_codigo == 3:  # Número mágico
            return "Entregue"
        elif self.status_codigo == 4:  # Número mágico (correspondendo ao "Cancelado")
            return "Cancelado"
        return "Desconhecido"


# Exemplo de uso
p1 = Pedido(1)  # O que significa 1?
print(f"Status P1: {p1.get_status_descricao()}")

p2 = Pedido(4)  # O que significa 4?
print(f"Status P2: {p2.get_status_descricao()}")
