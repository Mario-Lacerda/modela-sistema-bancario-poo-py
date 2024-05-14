# Desafios Dio - **Modelagem do Sistema Bancário em POO com Python**



## Sequência Projeto

### 1- Criando um sistema bancário com Python

Desafio básico onde foi proposto criar um sistema bancário simples em python. Esta será a v1 onde deve conter as operações de Saque, Depósito e Exibir extrato. As regras são: Limitado a 3 saques, limitado a R$500,00 de saques no total, todos os depósitos devem ser armazenados e exibidos no extrato, extrato deve exibir os valores depositados, sacados e o saldo atual em conta.


### 2- Otimizando o sistema bancário com funções

Neste desafio foi proposto otimizar o sistema criado anteriormente utilizando funções e outros conceitos como listas, dicionários entre outros aspectos, foi adicionado também a funcionalidade de exigir senha ao realizar login, criar usuários e criar contas podendo se criar mais de uma conta por usuário. Esta é a v2 do código.


### 3- Modelando o sistema bancário em POO

Terceira etapa deste desafio onde o sistema foi remodelado utilizando orientação a objetos. Realizando as mesmas tarefas da versão anterior porém com mais praticidade na criação por utilizar os conceitos de orientação a objetos como Herança, Polimorfismo, encapsulamento etc. Esta é a v3 do código.





# **Modelagem do Sistema Bancário em POO com Python**



**Classes:**

- **Conta:**
  - Atributos: número, saldo, titular
  - Métodos: depositar, sacar, transferir
- **Cliente:**
  - Atributos: nome, CPF, endereço
  - Métodos: criar_conta
- **Banco:**
  - Atributos: nome, clientes
  - Métodos: criar_cliente, criar_conta

**Exemplo de Código:**

python

```python
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
cliente1 = Cliente("Rose", "12345678900", "Rua c, 443")
conta1 = cliente1.criar_conta(banco)

cliente2 = Cliente("Mário", "98765432100", "Rua k, 395")
conta2 = cliente2.criar_conta(banco)

conta1.depositar(1000)
conta2.sacar(500)
conta1.transferir(200, conta2)

print(f"Saldo da conta 1: {conta1.saldo}")
print(f"Saldo da conta 2: {conta2.saldo}")
```



**Modelagem do Sistema Bancário em POO com Python (Detalhada e Abrangente)**

**Classes:**

- **Conta:**
  - Atributos:
    - `numero`: Número da conta
    - `saldo`: Saldo atual da conta
    - `titular`: Titular da conta
  - Métodos:
    - `depositar(valor)`: Deposita um valor na conta
    - `sacar(valor)`: Saca um valor da conta
    - `transferir(valor, conta_destino)`: Transfere um valor para outra conta
- **Cliente:**
  - Atributos:
    - `nome`: Nome do cliente
    - `CPF`: CPF do cliente
    - `endereco`: Endereço do cliente
  - Métodos:
    - `criar_conta(banco)`: Cria uma conta no banco informado
- **Banco:**
  - Atributos:
    - `nome`: Nome do banco
    - `clientes`: Lista de clientes do banco
  - Métodos:
    - `criar_cliente(cliente)`: Cria um novo cliente no banco
    - `criar_conta(cliente)`: Cria uma nova conta para um cliente



**Explicação Detalhada:**

- A classe `Conta` representa uma conta bancária e possui atributos para armazenar o número da conta, o saldo e o titular. Ela também possui métodos para depositar, sacar e transferir valores.
- A classe `Cliente` representa um cliente do banco e possui atributos para armazenar o nome, CPF e endereço do cliente. Ela possui um método para criar uma conta no banco.
- A classe `Banco` representa um banco e possui atributos para armazenar o nome do banco e uma lista de clientes. Ela possui métodos para criar novos clientes e criar novas contas para esses clientes.
- O exemplo de código mostra como criar um banco, dois clientes e duas contas. Em seguida, ele mostra como realizar operações bancárias básicas, como depósitos, saques e transferências.

Esta modelagem permite representar as principais entidades e operações de um sistema bancário. Ela pode ser estendida para incluir recursos adicionais, como histórico de transações, taxas e diferentes tipos de contas.