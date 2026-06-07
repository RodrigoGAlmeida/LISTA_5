matriz = []
linhas = int(input("Digite a quantidade de linhas: "))

for i in range(linhas):
    linha = input(f"Digite os elementos da linha {i} separados por espaço: ").split()
    matriz.append(linha)

invertida = []

for i in range(linhas-1,-1,-1):
      invertida.append(matriz[i])

for linha in invertida:
    print(linha)

