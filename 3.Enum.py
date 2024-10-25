from enum import Enum
import os

os .system("cls || clear")

class Sexo(Enum):
    MASCULINO = "masculino"
    FEMININO = "feminino"

# Aplicação.
print(f"Sexo: {Sexo.FEMININO}")
print(f"Sexo: {Sexo.FEMININO.name}")
print(f"Sexo: {Sexo.FEMININO.value}")    