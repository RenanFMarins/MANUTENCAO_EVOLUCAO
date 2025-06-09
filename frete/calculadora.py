from .enums import MetodoEnvio
from .estrategias import (
    EstrategiaCalculoFrete,
    CalculoFreteNormal,
    CalculoFreteExpresso,
    CalculoFreteSedex10,
    CalculoFreteRetirada,
)


class CalculadoraFrete:
    def __init__(self):
        self.estrategias: dict[MetodoEnvio, EstrategiaCalculoFrete] = {
            MetodoEnvio.NORMAL: CalculoFreteNormal(),
            MetodoEnvio.EXPRESSO: CalculoFreteExpresso(),
            MetodoEnvio.SEDEX_10: CalculoFreteSedex10(),
            MetodoEnvio.RETIRADA: CalculoFreteRetirada(),
        }

    def calcular(self, metodo: MetodoEnvio, peso_kg: float, distancia_km: float) -> float:
        estrategia = self.estrategias.get(metodo)
        if estrategia is None:
            print(f"Aviso: Método de envio '{metodo}' desconhecido.")
            return 0.0
        return estrategia.calcular(peso_kg, distancia_km)
