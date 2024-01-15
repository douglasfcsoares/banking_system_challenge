menu =  """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Valor a ser depositado: R$ '))
        if valor > 0:
            saldo += valor
            extrato += f'\nDepósito de R$ {valor:.2f}\n'
            print(f'Saldo atual: R$ {saldo:.2f}')
        
        else:
            print('Operação falhou o valor informado é inválido')

    elif opcao == 's':
        valor =  float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print('Operação falhou! o valor do saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print('Operação falhou! o valor informado é inválido')

    elif opcao == 'e':
        print('\n====================== EXTRATO ==========================')
        print(f'Não foram realizados movimentos.' if not extrato else extrato)
        print(f'\nSaldo: R$: {saldo:.2f}')
        print('=========================================================')

    elif opcao == 'q':
        print('Sair')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')