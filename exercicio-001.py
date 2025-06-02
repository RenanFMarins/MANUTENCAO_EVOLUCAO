def calc(val, d, t_rate):
    # val: valor do item
    # d: desconto
    # t_rate: taxa de juros
    v_d = val - (val*d)
    final = v_d + (v_d * t_rate)
    return final


# exemplo de uso
item_price = 100
discount_val = 0.1
tax = 0.05
print(calc(item_price, discount_val, tax))
