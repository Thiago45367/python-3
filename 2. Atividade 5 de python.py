import os
os.system("cls || clear")

# Dados do usuário.
print("\nSolicitando dados do usuário.")
nomeProdutos = input("\nEscreva do produto: ")
quantidade = int(input("\nEscreva a quantidade dos produtos: "))
precoDoproduto = float(input("\nEscreva o preço do produto: "))

# Soma.
somaDosprodutos = quantidade * precoDoproduto
valorTotal = somaDosprodutos - desconto

if quantidade <= 5:
    desconto: float = (somaDosprodutos * 2) / 100
elif quantidade > 5 and quantidade <= 10:
    desconto: float = (somaDosprodutos * 3) / 100
elif quantidade > 10:
    desconto: float = (somaDosprodutos * 5) / 100

subTotal = precoDoproduto * quantidade
totalPagar = subTotal - (subTotal * desconto)

# Resultados.
print("---Resultados---")
print(f"Nome do produto: {nomeProdutos}")
print(f"Quantidade do produto: {quantidade}")
print(f"Preço do produto: {precoDoproduto}")             