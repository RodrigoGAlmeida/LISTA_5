n = int(input("Digite o tamanho da matriz quadrada: "))
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        valor= int(input(f"Digite o valor da linha {i} coluna {j}: "))
        linha.append(valor)
    matriz.append(linha)

soma_princ = 0 
soma_sec = 0

for i in range(n):
    soma_princ += matriz[i][i]
    soma_sec += matriz[i][n-1-i]

print("Soma da diagonal principal: ", soma_princ)
print("Soma da diagonal secundaria: ", soma_sec)
