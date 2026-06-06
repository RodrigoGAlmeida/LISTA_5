#Recebe valor da divida
#Retorna valor dos juros, parcela, quantidade de parcelas e calor da parcela

divida = float(input("Digite o valor da divida: "))

parcelas = [1, 3, 6, 9, 12]
juros_parcela = [00.0, 10, 15, 20, 25]

print("Valor da Dívida | Valor dos Juros | Parcelas | Valor da Parcela")

for i in range(len(parcelas)):
    juros = divida * juros_parcela[i] / 100
    valor_total = divida + juros
    valor_parcela = valor_total / parcelas[i]

    print(f"R$ {valor_total:.2f} | R$ {juros:.2f} | {parcelas[i]} | R$ {valor_parcela:.2f}")