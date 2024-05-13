import os
import time
os.system("cls || clear")


soma : float = 0
quantidadeNotas = 0

while True :
    print("=== MENU ===")
    print("S - Inserir uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular média aritmética")
   
    resposta = input("Deseja inserir uma nota: ")
    resposta = resposta.upper()
   
    if  resposta == "S":
        nota = float(input("\nDigite uma nota: "))
        soma += nota
        quantidadeNotas += 1
    elif resposta == "P":
        if quantidadeNotas == 0:
            print("Não foram inseridas notas. \n")            
            input("Pressione uma tecla para continuar...")
            time.sleep(3)
        else:
            print(f"Quantidade de notas inseridas: {quantidadeNotas} \n")
            input("Pressione uma tecla para continuar...")
           
    elif resposta == "N":
        if quantidadeNotas == 0:
             print("Não foram inseridas notas. \n")
        else:
            break
    else:
        print("Opção inválida... \n")
        time.sleep(3)

media  = soma / quantidadeNotas

print(f"Média: {media}")