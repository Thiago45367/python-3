import os
os.system("cls || clear")



while True:
    notaUm = float(input("Escreva sua Primeira nota: "))
    notaDois = float(input("Escreva sua Segunda nota: "))

    if (notaUm < 0 or notaDois > 10) :
        print("Nota inválida.")
    else:
      break
   
somaDasnotas = notaUm + notaDois

media =  somaDasnotas / 2

print(f"\nNota informada: ")

print(f"\nPrimeira nota: {notaUm}")
print(f"\nSegunda nota: {notaDois}")
print(f"Media: {media}")