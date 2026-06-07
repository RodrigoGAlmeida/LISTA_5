termos = int(input("Digite o numero de termos: "))
soma = 0

for h in range(1,termos+1):
    soma = soma +(1/h)

print("O valor de H é: ",soma)