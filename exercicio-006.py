class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Estoque: {self.estoque}")


# Exemplo de uso
caneta = Produto("Caneta Azul", 1.50, 100)
caneta.exibir_detalhes()

# Modificação perigosa
caneta.preco = -5.0
caneta.estoque += 200
print("\nApós modificação direta:")
caneta.exibir_detalhes()
