# DESAFIO (Código e Python Vanilla)
    # Implementar 3 operações: depósito, saque e extrato.

# VERSÃO 1 - 
 
    # Operação de depósito:
        # - Trabalha somente com um usuário, então não precisaremos nos preocupar em identificar quel é o número da agência ou conta bancária.
        # - Todos os depósitos devem  ser armazenados em uma váriavel e exibidos na operação de extrato.
        # - O programa deve bloquear depósitos negativos.

    # Operação de saque:
        # - O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
        # - Não permitir saques caso o cliente não tenha saldo suficiente em conta.
        # - Todos os saque devem ser armazenados em uma variável e exibidos na operação de extrato.

    # Operação de extrato:
        # - O extrato deve listar todos os depósitos e saques realizados na conta.
        # - No fim da listagem deve ser exibido o saldo atual da conta.
        # - Os valores devem ser exibidos utilizando o formato R$ xxx,xx.

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor do depósito deve ser maior que zero.")

def sacar(valor):
    if numero_saques < LIMITE_SAQUES:
        if valor <= limite and valor <= saldo:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
    else:
        print("Operação falhou! Limite máximo de saques diários atingido.")

def exibir_extrato():
    print("\n==================== EXTRATO ====================")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        print("Obrigado e volte sempre!!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")