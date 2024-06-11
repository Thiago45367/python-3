'''Código em C.
float calcularMedia(float notas[]) {
	int i;
	float soma = 0;
	for(i = 0; i < TAM; i++) {
		soma += notas[i];
	}
	return soma / TAM;
}

char* verificarSituacao(float media) {
	char* resultado[200];
	media >= 7 ? strcpy(resultado, "Aprovado!") : strcpy(resultado, "Reprovado!");
	return resultado;
}

void mostrarResultado(float notas[]) {
	printf("\nMédia: %.1f \n", calcularMedia(notas));
	printf("Resultado: %s \n", verificarSituacao(calcularMedia(notas)));
}

int main() {
	setlocale(LC_ALL, "");
	
	float notas[TAM];
	int i;
	
	for(i = 0; i < TAM; i++) {
		printf("Digite a %dª nota: ", i + 1);
		scanf("%f",&notas[i]);
	}

	mostrarResultado(notas);
	
	return 0;
}
'''
#Código em python.
import os
os.system("cls || clear")

# Vetores.

QUANTIDADE_NOTAS = 3
notas = []

# Dados do usuario.
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Escreva uma nota: "))
    notas.append(nota)

for i in range(3):
    print(f"{i+1}ª nota: {notas}")

media = sum(notas) / QUANTIDADE_NOTAS

# Exibindo Resultados.
print("\nExibindo resultados")

os.system("cls || clear")
x = 1
for i in notas:
    print(f"{x}ª nota: {nota}")
    x += 1
print(f"Média: {media}") 

if media >= 7:
    print("\nAprovado.")
else:
    print("\nReprovado.")
