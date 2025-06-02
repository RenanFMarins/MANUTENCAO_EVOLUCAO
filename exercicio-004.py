def calcular_desconto_cliente(tipo_cliente, valor_compra, compras_anteriores):
    desconto = 0
    if tipo_cliente == "OURO":
        if valor_compra > 200:
            desconto = 0.15
            if compras_anteriores > 10:
                desconto += 0.05  # Bônus por lealdade
        else:
            desconto = 0.10
    elif tipo_cliente == "PRATA":
        if valor_compra > 150:
            desconto = 0.10
        else:
            desconto = 0.05
    else:  # BRONZE ou novo cliente
        if valor_compra > 100:
            desconto = 0.05
    return desconto


print(f"Desconto Ouro (>200, >10 compras): {calcular_desconto_cliente('OURO', 250, 12)}")
print(f"Desconto Prata (<=150): {calcular_desconto_cliente('PRATA', 100, 3)}")
