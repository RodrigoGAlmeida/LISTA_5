total = 0
while True:
    codigo = int(input("Digite o código do produto (0 para encerrar): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade: "))

    if codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.30
    elif codigo == 105:
        preco = 1.00
    else:
        print("Código invalido")
        continue

valor_item = preco * quantidade
total += valor_item

print(f"\nTotal do pedido: R${total:.2f}")