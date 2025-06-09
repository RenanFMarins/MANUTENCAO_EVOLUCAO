class Produto:
    def __init__(self, nome, preco, estoque):
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_estoque(estoque)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco < 0:
            print("Erro: preço não pode ser negativo. Atribuição ignorada.")
            return
        self.__preco = preco

    def set_estoque(self, estoque):
        if estoque < 0:
            print("Erro: estoque não pode ser negativo. Atribuição ignorada.")
            return
        self.__estoque = estoque

    def exibir_detalhes(self):
        print(f"Produto: {self.__nome}, Preço: R${self.__preco:.2f}, Estoque: {self.__estoque}")


caneta = Produto("Caneta Azul", 1.50, 100)
caneta.exibir_detalhes()

caneta.set_estoque(caneta.get_estoque() + 200)

print("\nApós modificações controladas:")
caneta.exibir_detalhes()
