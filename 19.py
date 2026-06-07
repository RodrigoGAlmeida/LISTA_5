texto = input("Digite o texto: ").lower()
vogais = 0
consoante = 0

for i in range(len(texto)):
    if texto[i] in "aeiou":
        vogais += 1
    else:
        consoante += 1

print("\nNumero de vogais: ",vogais)
print("Numero de consoantes: ",consoante)
