import os
os.system("cls || clear")

# variaveis.
valorUm = int(input("\nDigite o primeiro valor: "))
valorDois = int(input("\nDigite o segundo valor: "))
operacao = str(input ("\nDigite a operação: "))

match(operacao):

    case '+':
        resultado = valorUm + valorDois
    case '-':
        resultado = valorUm - valorDois
    case '*':
        resultado = valorUm * valorDois
    case '/':
        resultado = valorUm / valorDois
    case _:
        resultado = 0

print(f"Primeiro número : {valorUm}")
print (f"Segundo número : {valorDois}")
print(f"Resultado : {resultado}")              