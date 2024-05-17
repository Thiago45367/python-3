import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3

notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Escreva uma nota: "))
    notas.append(nota)

for i in range(3):
    print(f"Nota: {notas[i]}")

media = sum(notas) / QUANTIDADE_NOTAS

print("\nExibindo resultados")

for nota in notas:
    print(f"NOTA: {nota}")

print(f"Média: {media}") 