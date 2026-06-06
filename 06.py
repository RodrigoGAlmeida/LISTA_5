#recebe o nome do atleta, 5 notas
#informa o nome, as 5 notas, maior nota, menor nota e media das 3 notas medianas

while True:
    nome = input("Nome do atleta: ")

    if nome == "":
        break

    saltos = []

    for i in range(5):
        salto = float(input(f"Digite a nota do {i+1} salto: "))
        saltos.append(salto)

    melhor = max(saltos)
    pior = min(saltos)

    media = (sum(saltos) - melhor - pior) / 3

    print(f"Atleta: {nome}")
    print("")
    for j in range(5):
        posição = ["primeiro","Segundo","Terceiro", "Quarto","Quinto"]
        print(F"{posição[j]} salto: {saltos[j]} m")
    print(f"Melhor salto: {melhor:.1f} m")
    print(f"Pior Salto:{pior:.1f} m")
    print(f"Média dos demais saltos: {media:.1f} m")
