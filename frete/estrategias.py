from abc import ABC, abstractmethod


class EstrategiaCalculoFrete(ABC):
    @abstractmethod
    def calcular(self, peso_kg: float, distancia_km: float) -> float:
        pass


class CalculoFreteNormal(EstrategiaCalculoFrete):
    def calcular(self, peso_kg: float, distancia_km: float) -> float:
        return 5.0 + (peso_kg * 1.5) + (distancia_km * 0.10)


class CalculoFreteExpresso(EstrategiaCalculoFrete):
    def calcular(self, peso_kg: float, distancia_km: float) -> float:
        return 5.0 * 1.5 + (peso_kg * 2.0) + (distancia_km * 0.15)


class CalculoFreteSedex10(EstrategiaCalculoFrete):
    def calcular(self, peso_kg: float, distancia_km: float) -> float:
        return 5.0 * 2.0 + (peso_kg * 2.5) + (distancia_km * 0.20) + 10.0


class CalculoFreteRetirada(EstrategiaCalculoFrete):
    def calcular(self, peso_kg: float, distancia_km: float) -> float:
        return 0.0
