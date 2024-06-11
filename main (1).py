import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    
    # Calculo dos dados digitados.
    pesoIMC = peso / (altura * altura)
    
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    
    if pesoIMC < 18.5:
        print("Conclusão: Abaixo do peso")
    elif pesoIMC >= 18.5 and pesoIMC < 25:
        print("Conclusão: Peso normal")
    elif pesoIMC >= 25 and pesoIMC < 30:
        print("Conclusão: Sobrepeso")
    elif pesoIMC >= 30 and pesoIMC < 35:
        print("Conclusão: Obesidade grau I")
    elif pesoIMC >= 35 and pesoIMC < 40:
        print("Conclusão: Obesidade grau II")
    elif pesoIMC >= 40:
        print("Conclusão: Obesidade grau III")
    else:
        print("OPÇÃO NEGADO!")
    print()


