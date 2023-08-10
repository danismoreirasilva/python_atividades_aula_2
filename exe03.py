#Sem validação se a opção é um número ou outro caractere
saldo = 0.0
opcao = 0
repetir = True
while repetir:
    while opcao != 4:
        print('Menu'.center(30, '='))
        print('1 - Consulta Saldo')
        print('2 - Saque')
        print('3 - Depósito')
        print('4 - Sair')
        print(''.center(30, '='))

        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            print(f'Seu saldo é de: R$ {saldo:.2f}!')
        elif opcao == 2:
            if saldo == 0.0:
                print(f'Saldo insuficente para qualquer valor de saque!')
            else:
                valor = float(input('Digite o valor do saque: R$ '))
                if valor > saldo:
                    print(f'Saldo insuficente para o saque de R$ {valor}!\n Saldo atual: R$ {saldo}')
                elif valor > 0:
                        saldo -= valor
                        print(f'Saque realizado com sucesso!')
                else:
                    print(f'Operação não realizada, valor deve ser maior do que 0!')
        elif opcao == 3:
            valor = float(input('Digite o valor do depósito: R$ '))
            if valor > 0:
                saldo += valor
                print(f'Depósito realizado com sucesso!')
            else:
                print(f'Operação não realizada, valor deve ser maior do que 0!')
        elif opcao == 4:
            break
        else:
            print(f'Você digitou uma opção inválida. Digite novamente!')

    print(f'Você saiu do programa!')
    repetir = False