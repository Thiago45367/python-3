import os
os.system("cls || clear")

nota = float(input("Escreva uma nota: "))

while (nota < 0 or nota > 10) :
    nota = float(input("Escreva uma nota: "))

print(f"Nota informada: {nota}")

print("\n==== Fim ====\n")