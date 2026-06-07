#mostre os n termos da série 1/1 + 2/3 + 3/5 ...

termos = []
soma = 0
quantidade = int(input("Digite a quantidade de termos: "))

denominador = 1
for i in range(1, quantidade + 1):
    soma += i / denominador
    if i == quantidade:
        termo = f"{i}/{denominador}."
    else:
        termo = f"{i}/{denominador} + "
    termos.append(termo)
    denominador += 2

print("S = " + "".join(termos))
print("A soma dos termos é: ", soma)

