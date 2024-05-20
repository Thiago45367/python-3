import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 4
notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Escreva uma nota: "))
    notas.append(nota)

for i in range(4):
    print(f"{i+1}ª nota: {notas[i]}")

media = sum(notas) / QUANTIDADE_NOTAS

print("\nExibindo resultados")

for nota in enumerate(notas):
    print(f"{i+1}ª nota: {nota}")

print(f"Média: {media}") 