matriz = []
linhas = int(input("DIgite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor da linha {i} coluna {j}: "))
        linha.append(valor)
    matriz.append(linha)

elemento = int(input("Digite o elemento que deseja procurar: "))
contador = 0

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == elemento:
            contador += 1

if contador == 1:
    print(f"O elemento {elemento} aparece {contador} vez na matriz.")
else:
        print(f"O elemento {elemento} aparece {contador} vezes na matriz.")