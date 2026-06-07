matriz = []
linhas = int(input("Digite a quantidade de linhas: "))

for i in range(linhas):
    linha = input(f"Digite os elementos da linha {i} separados por espaço: ").split()
    matriz.append(linha)

mesmo_tamanho = True
tamanho_colunas = len(matriz[0])

for linha in matriz:
    if len(linha) != tamanho_colunas:
        mesmo_tamanho = False

quadrada = linhas == tamanho_colunas
print(quadrada and mesmo_tamanho)