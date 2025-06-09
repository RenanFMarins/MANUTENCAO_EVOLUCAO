class Pedido:
    STATUS_PENDENTE = 0
    STATUS_PROCESSANDO = 1
    STATUS_ENVIADO = 2
    STATUS_ENTREGUE = 3
    STATUS_CANCELADO = 4

    def __init__(self, status_codigo):
        self.status_codigo = status_codigo

    def get_status_descricao(self):
        if self.status_codigo == Pedido.STATUS_PENDENTE:
            return "Pendente"
        elif self.status_codigo == Pedido.STATUS_PROCESSANDO:
            return "Processando"
        elif self.status_codigo == Pedido.STATUS_ENVIADO:
            return "Enviado"
        elif self.status_codigo == Pedido.STATUS_ENTREGUE:
            return "Entregue"
        elif self.status_codigo == Pedido.STATUS_CANCELADO:
            return "Cancelado"
        return "Desconhecido"


p1 = Pedido(Pedido.STATUS_PROCESSANDO)
print(f"Status P1: {p1.get_status_descricao()}")

p2 = Pedido(Pedido.STATUS_CANCELADO)
print(f"Status P2: {p2.get_status_descricao()}")
