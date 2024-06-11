import os
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade : int
    peso : float
    altura : float

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Escreva seu nome: ")
    idade = int(input("Escreva sua idade: "))
    peso = float(input("Escreva seu peso: "))
    altura = float(input("Escreva sua altura: "))
    aluno = Aluno(nome = nome, idade = idade, peso = peso, altura = altura)
    alunos.append(aluno)

for dados_aluno in alunos:
    print(f"Nome: {dados_aluno.nome}")
    print(f"Idade: {dados_aluno.idade}")
    print(f"Peso: {dados_aluno.peso}")
    print(f"Altura: {dados_aluno.altura}")