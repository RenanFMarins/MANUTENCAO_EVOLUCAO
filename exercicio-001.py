def calcular_preco_final_item(preco_bruto, percentual_desconto, taxa_imposto):
    preco_com_desconto = preco_bruto - (preco_bruto * percentual_desconto)
    preco_final = preco_com_desconto + (preco_com_desconto * taxa_imposto)
    return preco_final


preco_item = 100
desconto = 0.1
imposto = 0.05

print(calcular_preco_final_item(preco_item, desconto, imposto))
