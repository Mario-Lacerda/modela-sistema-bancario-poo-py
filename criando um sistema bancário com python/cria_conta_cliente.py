class Conta:
    def __init__(self, numero, saldo, titular):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
        else:
            print("Saldo insuficiente")


class Cliente:
    def __init__(self, nome, CPF, endereco):
        self.nome = nome
        self.CPF = CPF
        self.endereco = endereco

    def criar_conta(self, banco):
        conta = banco.criar_conta(self)
        return conta


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def criar_cliente(self, cliente):
        self.clientes.append(cliente)

    def criar_conta(self, cliente):
        numero = len(self.clientes) + 1
        conta = Conta(numero, 0, cliente)
        return conta


# Exemplo de uso

banco = Banco("Banco do Brasil")
cliente1 = Cliente("Pedro", "12345678900", "Rua A, 123")
conta1 = cliente1.criar_conta(banco)

cliente2 = Cliente("Mercia", "98765432100", "Rua B, 456")
conta2 = cliente2.criar_conta(banco)

conta1.depositar(1000)
conta2.sacar(500)
conta1.transferir(200, conta2)

print(f"Saldo da conta 1: {conta1.saldo}")
print(f"Saldo da conta 2: {conta2.saldo}")
