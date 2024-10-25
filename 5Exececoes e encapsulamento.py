import os

os .system("cls || clear")

# Crianda minha própria exceção.
class SaldoInsuficienteError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido.

    # Semelhante ao getSaldo()
    @property
    def saldo(self):
        return self._saldo

    def sacar(self) -> str:
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        try:
            self.__verificar_sacar(valor_saque)
        except SaldoInsuficienteError as erro:
            return f"Prezado cliente: {erro}"

        return f"Saque realizado com sucesso."

    def __verificar_sacar(self, valor) -> None: # Método privado.
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass

# Instanciando classe.
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaCorrente(444, 555)

print(f"Número da conta: {conta_corrente.numero_conta}")
print(f"Saldo: {conta_corrente.saldo}")

# Sacar com saldo insuficiente.
print("Conta corrente")
print(conta_corrente.sacar())
print(f"Saldo: {conta_corrente.saldo}")

print("Conta poupança")
print(conta_poupanca.sacar())
print(f"Saldo: {conta_poupanca.saldo}")