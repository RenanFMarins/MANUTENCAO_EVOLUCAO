def calcular_desconto_cliente(tipo_cliente, valor_compra, compras_anteriores):
    if tipo_cliente == "OURO":
        return calcular_desconto_ouro(valor_compra, compras_anteriores)

    if tipo_cliente == "PRATA":
        return 0.10 if valor_compra > 150 else 0.05

    if valor_compra > 100:
        return 0.05

    return 0.0


def calcular_desconto_ouro(valor_compra, compras_anteriores):
    if valor_compra > 200:
        bonus_fidelidade = 0.05 if compras_anteriores > 10 else 0.0
        return 0.15 + bonus_fidelidade
    return 0.10


print(f"Desconto Ouro (>200, >10 compras): {calcular_desconto_cliente('OURO', 250, 12)}")
print(f"Desconto Prata (<=150): {calcular_desconto_cliente('PRATA', 100, 3)}")
print(f"Desconto Bronze (>100): {calcular_desconto_cliente('BRONZE', 120, 0)}")
print(f"Sem desconto (BRONZE, <100): {calcular_desconto_cliente('BRONZE', 80, 0)}")
