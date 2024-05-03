import os
os.system("cls || clear")

# Dados do usuário.
print("Solicitando dados para o usuário.")
nome = input("Escreva seu nome: ")
idade = int(input("Escreva sua idade: "))
notaUm = float(input("Escreva sua Primeiro nota: "))
notaDois = float(input("Escreva sua Segunda nota: "))
notaTres = float(input("Escreva sua Teceira nota: "))

somaDasnotas = notaUm + notaDois + notaTres

# Soma.
media = somaDasnotas / 2

print("\nExibindo dados do usuário.")
print(f"Nome : {nome}")
print(f"Idade : {idade}")
print(f"Primeira Nota: {notaUm}")
print(f"Segunda Nota: {notaDois}")
print(f"Teceira Nota: {notaTres}")
print(f"Media: {media}")

if media >= 7:
    print("\nAprovado")
else:
    print("\nReprovado")