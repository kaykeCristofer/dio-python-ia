def depositar(*, saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return saldo, extrato

        else:
            print("Operação falhou! O valor informado é inválido.")

def sacar(saldo, valor, extrato, numero_saques, LIMITE_SAQUES, limite, /):
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            return saldo, extrato, numero_saques

        else:
            print("Operação falhou! O valor informado é inválido.")

def extrato(saldo, /, *, extrato="extrato"):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário: ")
    cpf = int(input("Informe o CPF do usuário: "))
    endereco = input("Informe o endereço do usuário: ")
    
    cliente = (nome, data_nascimento, cpf, endereco)

    for cpf in cliente:
        if cpf == cliente[2]:
            print("CPF já cadastrado.")
            break
    
    usuarios.append(cliente)
    print("Usuário cadastrado com sucesso!")
    

def cadastrar_conta_bancaria(AGENTE, numero_conta, usuarios):
    cpf = int(input("Informe o CPF do usuário: "))

    for usuario in usuarios:
        if cpf == usuario[2]:
            conta = (AGENCIA, numero_conta, usuario)
            contas.append(conta)
            print("Conta cadastrada com sucesso!")
            break

    else:
        print("Usuário não encontrado.")
        return
    

if __name__ == "__main__":

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [q] Sair
    

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(valor)

        elif opcao == "e":
            extrato(saldo, extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            cadastrar_conta_bancaria(AGENCIA, numero_conta, usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")