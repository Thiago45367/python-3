import os

os .system("cls || clear") # limpa op terminal.

# Criando a classe Aluno.
class Aluno: 
    # Criando um construtor.
    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"


# Instanciar classe.
aluno = Aluno("Alex", 22)

# print(aluno.nome)
# print(aluno.idade)

print(aluno.exibir_dados())