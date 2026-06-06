votos = [0, 0, 0, 0, 0, 0]

while True:
    voto = int(input("Digite o voto (0 para encerrar): "))

    if voto == 0:
        break

    if 1 <= voto <= 6:
        votos[voto - 1] += 1
    else:
        print("Voto inválido!")

total = sum(votos)

if total > 0:
    perc_nulos = (votos[4] / total) * 100
    perc_brancos = (votos[5] / total) * 100
else:
    perc_nulos = 0
    perc_brancos = 0

print("\nResultado da eleição")
print("José:", votos[0], "votos")
print("João:", votos[1], "votos")
print("Maria:", votos[2], "votos")
print("Ana:", votos[3], "votos")
print("Nulos:", votos[4], "votos")
print("Brancos:", votos[5], "votos")
print(f"Percentual de nulos: {perc_nulos:.2f}%")
print(f"Percentual de brancos: {perc_brancos:.2f}%")