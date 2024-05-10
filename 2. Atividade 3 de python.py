import os
os.system("cls || clear")

# Tipagem dinâmica.

# Atribuindo valores
print("Solicitando dados para o usuário.")
login = input("Escreva o login: ")
senha = input("Escreva a senha: ")

if login =="BOB@3" and senha == "123":
    print("Bem-vindo!")
else:
    print("Acesso negado!")

