menu = """

    Pressione [d] para depositar um valor.
    Pressione [s] para efetuar um saque. 
    Pressione [e] para retirar seu extrato. 
    Pressione [q] para cancelar a operação.

==> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else: 
            print("Operação falhou! O valor inserido é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: R$"))

        excedeu_saldo = valor > saldo

        excedeu_valor = valor > limite

        excedeu_limite = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo: 
            print("Operação falhou! Você não possui saldo suficiente.")

        elif excedeu_valor:
            print("Operação falhou! O valor limite do saque foi excedido.")

        elif excedeu_limite:
            print("Operação falhou! Você excedeu o número máximo de saques.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numeros_saques += 1
        
        else: 
            print("Operação falhou! O valor inserido inválido.")
    
    elif opcao == "e":
        print("Nenhuma movimentação foi realizada." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("====================================")
    
    elif opcao == "q":
        break

    else: 
        print("Operação inválida, selecione uma operação novamente.")