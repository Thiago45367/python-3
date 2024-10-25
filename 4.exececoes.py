import os

os .system("cls || clear")

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido.

class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass

# Instanciand classe.
conta_corrente = ContaCorrente(22, 333)

print(f"Saldo: {conta_corrente._saldo}")