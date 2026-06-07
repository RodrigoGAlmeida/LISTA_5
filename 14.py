matriz = []
linhas = int(input("DIgite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor da linha {i} coluna {j}: "))
        linha.append(valor)
    matriz.append(linha)

transposta = []

for j in range(colunas):
    nova_linha = []
    for i in range(linhas):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

    print("\nMatriz Original:")
    for linha in matriz:
        print(linha)

    print("\nMatriz Transposta:")
    for linha in transposta:
        print(linha)
