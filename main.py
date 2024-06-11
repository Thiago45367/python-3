import os
import time
os.system("cls || clear")

menu = {
    "1": {"nome": "Macarrão com Almôndega", "preco": 9.17},
    "2": {"nome": "Pizza", "preco": 14.99},
    "3": {"nome": "Lasanha", "preco": 8.00},
    "4": {"nome": "Moqueca", "preco": 21.99},
    "5": {"nome": "Tapioca", "preco": 13.99},
    "6": {"nome": "Strogonoff", "preco": 19.99},
    "7": {"nome": "Picanha", "preco": 1171.73}
}

ordem = []

while True :
    print("=== MENU ===")
    print("----------------------------")
    print("1 - Macarrão com Almôndega - R$ 9,17")
    print("2 - Pizza - R$ 14,99")
    print("3 - Lasanha - R$ 8,00")
    print("4 - Moqueca - R$ 21,99")
    print("5 - Tapioca - 13,99 ")
    print("6 - Strogonoff - R$ 19,99")
    print("7 - Picanha - R$ 1.171,73")
    print("----------------------------")
    
    cardapio = input("Deseja sua comida: ")
    cardapio = cardapio.upper()
    os.system("cls || clear")
    
    if cardapio == "0":
        break
    
    if cardapio in menu:
        ordem.append(menu[cardapio])
        print(f"\n{menu[cardapio]['nome']} adicionando ao pedido.")
    else:
        print("\nOpção inválida...\n")
    time.sleep(2)

total = sum(item["preco"] for item in ordem)

if total == 0:
    print("Nenhum pedido foi realizado.")
else:
    print("Resumo do pedido:")
    for item in ordem:
        print(f"{item['nome']} - R$ {item['preco']:.2f}")
    print(f"Subtotal: R$ {total:.2f}")
    
    pagamento = input("Forma de pagamento (A - à vista, P - a prazo): ").upper()

if pagamento == "A":
    desconto = total * 0.10
    total_a_pagar = total - desconto
    print(f"Desconto: R$ {desconto:.2f}")
elif pagamento == "P":
    acrescimo = total * 0.10
    total_a_pagar = total + acrescimo
    print(f"Acréscimo: R$ {acrescimo:.2f}")
else:
    print("Forma de pagamento inválida. Calculando valor sem desconto/acréscimo.")
    total_a_pagar = total 
    
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
