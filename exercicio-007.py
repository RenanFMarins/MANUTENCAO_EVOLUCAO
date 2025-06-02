from enum import Enum


class MetodoEnvio(Enum):
    NORMAL = 1
    EXPRESSO = 2
    SEDEX_10 = 3


class CalculadoraFrete:
    def calcular(self, metodo: MetodoEnvio, peso_kg: float, distancia_km: float) -> float:
        custo_base = 5.0

        if metodo == MetodoEnvio.NORMAL:
            return custo_base + (peso_kg * 1.5) + (distancia_km * 0.10)
        elif metodo == MetodoEnvio.EXPRESSO:
            return custo_base * 1.5 + (peso_kg * 2.0) + (distancia_km * 0.15)
        elif metodo == MetodoEnvio.SEDEX_10:
            return custo_base * 2.0 + (peso_kg * 2.5) + (distancia_km * 0.20) + 10.0  # taxa extra
        else:
            print(f"Aviso: Método de envio '{metodo}' desconhecido.")
            return 0.0


# Exemplo de uso
calc = CalculadoraFrete()
print(f"Frete Normal: R${calc.calcular(MetodoEnvio.NORMAL, 2.0, 100.0):.2f}")
print(f"Frete Expresso: R${calc.calcular(MetodoEnvio.EXPRESSO, 2.0, 100.0):.2f}")
print(f"Frete Sedex 10: R${calc.calcular(MetodoEnvio.SEDEX_10, 2.0, 100.0):.2f}")
