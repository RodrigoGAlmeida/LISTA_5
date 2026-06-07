matriz = []
linhas = int(input("DIgite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = i * j
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz: ")
for linha in matriz:
    print(linha)