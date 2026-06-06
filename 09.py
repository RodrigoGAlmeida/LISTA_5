n = int(input("Digite a quantidade de termos: "))

soma = 0
denominador = 1

for numerador in range(1,n+1):
    termo = numerador/ denominador
    soma += termo
    
    print(f"{numerador}/{denominador}",end=" ")

    denominador+=2

print(f"Soma da série = {soma:.2f}")