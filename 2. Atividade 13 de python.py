import os
os.system("cls || clear")

soma = 0


for i in range(1, 3):
    while True :
        notas = float(input(f"Escreva sua {i}º nota: "))

        if notas > 10 or notas < 0:
            print("Nota inválida")
        else:
            soma += notas
            break

# Exibindo Resultados.
media : float = soma / i

print("===Resultados===")
print(f"Media: {media}")