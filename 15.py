matriz = []
linhas = int(input("DIgite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor da linha {i} coluna {j}: "))
        linha.append(valor)
    matriz.append(linha)

maior = 0
menor = 9999999999999999999999999999

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
             menor = matriz[i][j]


print("\nO maior elemento é: ",maior)
print("O menor elemento é: ",menor)