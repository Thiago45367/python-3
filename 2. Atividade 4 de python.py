import os
os.system("cls || clear")

nome = input("Escreva seu nome: ")
idade = int(input("Escreva sua idade: "))

if idade < 16:
    print("\nNão pode votar.")
elif idade < 18:
    print("\nvoto opcional.")
elif idade < 65:
    print("\nvoto obrigatório.")
else:
    print("\nNão obrigatório.")            