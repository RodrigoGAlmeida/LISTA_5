intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

numero=float(input("Digite um número(-1 para sair): "))

while numero >= 0:
    if numero <= 25:
        intervalo1 += 1
    elif numero <= 50:
        intervalo2 += 1
    elif numero <= 75:
        intervalo3 += 1
    else:
        intervalo4 += 1

    numero=float(input("Digite um número(-1 para sair): "))

print("\nQuantidade de números em cada intervalo:")
print(f"Intervalo 1 (0-25): {intervalo1}")
print(f"Intervalo 2 (26-50): {intervalo2}")
print(f"Intervalo 3 (51-75): {intervalo3}")
print(f"Intervalo 4 (76-100): {intervalo4}")

