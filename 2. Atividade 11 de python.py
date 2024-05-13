import os
os.system("cls || clear")

print("\nSolicitando dados para o usuário.")
nome = input("Escreva o nome do aluno: ")
notaUm = float(input("Escreva sua Primeiro nota: "))
notaDois = float(input("Escreva sua Segunda nota: "))

while (notaUm < 0 or notaDois > 10) :
    notaUm = float(input("Escreva sua Primeiro nota: "))
    notaDois = float(input("Escreva sua Segunda nota: "))

somaDasnotas = notaUm + notaDois

media =  somaDasnotas / 2

print(f"Nota informada: ")

print(f"Primeira nota: {notaUm}")
print(f"Segunda nota: {notaDois}")
print(f"Media: {media}")