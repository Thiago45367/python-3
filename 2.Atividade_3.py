from enum import Enum
import os

os .system("cls || clear")

class Sexo(Enum):
    MASCULINO = "masculino"
    FEMININO = "feminino"

class Setor(Enum):
    FINNANCEIRO = "finaceiro"
    RECURSOS_HUMANOS = "recursos humanos"
    VENDAS = "vendas"
    MARKETING = "marketing"

class Funcionario:

    def __init__(self, nome: str, idade: int, id: str, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.nome: str = nome
        self.idade: int = idade
        self.salario: float = salario
        self.setor: setor = setor
        self.sexo: sexo = sexo
    
    def exibir_dados(self) -> str:
        return ( f"Nome: {self.nome}"
                 f"\nIdade: {self.idade}"
                 f"\nSalario: {self.salario}"
                 f"\nSetor: {self.setor}"
                 f"\nSexo: {self.sexo.value}"  
               )
    
Funcionario = Funcionario("Jonh Boston", 22 ,"25362566", 679.60, Setor.RECURSOS_HUMANOS, Sexo.MASCULINO)

print(Funcionario.exibir_dados())