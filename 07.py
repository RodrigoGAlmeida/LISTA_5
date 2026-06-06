#recebe o nome do atleta, 57 notas
#informa o nome, as 7 notas, maior nota, menor nota e media das 3 notas medianas

while True:
    nome = input("Nome do atleta: ")

    if nome == "":
        break

    notas = []

    for i in range(7):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    melhor = max(notas)
    pior = min(notas)

    media = (sum(notas) - melhor - pior) / 3

    print(f"Atleta: {nome}")
    for j in range(7):
        print(F"Nota: {notas[j]}")
    print("")

    print("Resultado Final:")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {melhor:.1f}")
    print(f"Pior nota:{pior:.1f}")
    print(f"Média: {media:.2f}")
