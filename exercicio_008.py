def processar_pedidos_por_categoria(pedidos, categoria_alvo):
    produtos_encontrados = []
    total_valor = 0

    for pedido in pedidos:
        print(f"\nProcessando Pedido ID: {pedido['id']}")
        produtos, subtotal = filtrar_itens_por_categoria(pedido, categoria_alvo)
        produtos_encontrados.extend(produtos)
        total_valor += subtotal

    print(f"\nTotal de produtos da categoria '{categoria_alvo}': {len(produtos_encontrados)}")
    print(f"Valor total: R${total_valor:.2f}")

    return produtos_encontrados, total_valor


def filtrar_itens_por_categoria(pedido, categoria_alvo):
    produtos = []
    subtotal = 0

    for item in pedido.get("itens", []):
        if item.get("categoria") == categoria_alvo:
            print(f"  → Encontrado: {item['nome_produto']} (R${item['preco']})")
            produtos.append(item["nome_produto"])
            subtotal += item["preco"]

    return produtos, subtotal


lista_pedidos = [
    {
        "id": "P001",
        "itens": [
            {"nome_produto": "Laptop Gamer", "categoria": "Eletrônicos", "preco": 7500.00},
            {"nome_produto": "Mouse Sem Fio", "categoria": "Acessórios", "preco": 150.00}
        ]
    },
    {
        "id": "P002",
        "itens": [
            {"nome_produto": "Teclado Mecânico", "categoria": "Acessórios", "preco": 450.00},
            {"nome_produto": "Monitor Ultrawide", "categoria": "Eletrônicos", "preco": 2200.00},
            {"nome_produto": "SSD 1TB", "categoria": "Eletrônicos", "preco": 600.00}
        ]
    }
]

processar_pedidos_por_categoria(lista_pedidos, "Eletrônicos")
