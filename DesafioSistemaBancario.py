menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
VERIFICA_LIMIES_SAQUES = LIMITE_SAQUES >= numero_saques

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor_deposito = int(input("Quanto deseja depositar? "))
        if valor_deposito>0:
            deposito = valor_deposito
            saldo += deposito
        else:
            print("Por favor, informe um valor posiivo.")

    elif opcao == "s":
        print("Saque")
        valor_saque = int(input("Quanto deseja sacar? "))
        if VERIFICA_LIMIES_SAQUES == False:
            print("Voçê ja aingiu o valor maximo de saques diarios, por favor volte amanha.")
        elif valor_saque < saldo:
            saldo -= valor_saque
            numero_saques += 1
        elif valor_saque > saldo and valor_saque < limite:
            limite -= abs((saldo-valor_saque))
            numero_saques += 1
        else:
            print("Voçê não possui saldo o suficiente para esta operação.")

    elif opcao == "e":
        print("Extrato")
        print(f"Valores depositados: R${deposito}")
        print(f"Saque: R${valor_saque}")


        print(f"Saldo: R${saldo}")

    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Operação invalida, por favor selecione a operação desejada.")