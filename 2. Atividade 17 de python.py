import os
os.system("cls || clear")

quantidade_negativos = 0
quantidade_positivos = 0
maior_numero = 0
menor_numero = 0
soma_geral = 0
QUANTIDADE_NUMEROS = 5
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Escreva um número: "))
    numeros.append(numero)

for i in range(5):
    print(f"Número: {numeros}")

    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1
    else:
        print("=== Erro na leitura! ===")

maior_numero = max(maior_numero, numero)
menor_numero = min(menor_numero, numero)

soma_geral += numero

print("\nExibindo Números: ")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")