import os
os.system("cls || clear")

# Na linguagem de programação C.
# float notas[5];

# Vetor me Python.
notas = []

for i in range(3):
    nota = float(input("Escreva uma nota: "))
    notas.append(nota)

for i in range(3):
    print(f"Nota: {notas[i]}")
