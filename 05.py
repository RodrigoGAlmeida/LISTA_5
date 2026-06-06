gabarito = []

print("Digite o gabarito da prova:")

for i in range(10):
    resposta = input(f"Questão {i+1}: ").upper()
    gabarito.append(resposta)

print("\n" *50)

total_alunos = 0
soma_notas = 0
maior_nota = 0
menor_nota = 10
aluno_maior = ""
aluno_menor = ""

while True:

    acertos = 0
    print("Responda: A/B/C/D/E")
    aluno = input("Digite o nome: ")

    for i in range(10):
        resposta = input(f"Resposta da questão {i+1}: ").upper()

        if resposta == gabarito[i]:
            acertos += 1

    print(f"Nota do aluno: {acertos}")

    total_alunos += 1
    soma_notas += acertos

    if acertos > maior_nota:
        maior_nota = acertos
        aluno_maior = aluno

    if acertos < menor_nota:
        menor_nota = acertos
        aluno_menor = aluno

    continuar = input("Outro aluno? (S/N): ").upper()

    if continuar == "N":
        break

media = soma_notas / total_alunos

print("\nRELATÓRIO FINAL")
print("Maior nota:", maior_nota)
print("Aluno com a maior nota:", aluno_maior)
print("Menor nota:", menor_nota)
print("Aluno com a menor nota:", aluno_menor)
print("Total de alunos:", total_alunos)
print(f"Média da turma: {media:.2f}")