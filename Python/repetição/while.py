#  While
import time
opcao = ''
saldo = 2500

while opcao != 0:
    opcao = int(input('[1] Saque | [2] Extrato [0] Sair \nDigite a opção: '))
    if opcao == 1:
        saque = int(input('Informe o valor do saque R$: '))
        if saque <= saldo:
            time.sleep(2)
            print('Contando cédulas...')
            time.sleep(2)
            print('Saque realizado com sucesso')
        else:
            print('Saldo insuficiente para saque!')
    elif opcao == 2:
        extrato_atualizado = saldo - saque
        print(f'Exrato atual: R$ {extrato_atualizado}')
    elif opcao == 0:
        time.sleep(2)
        print('Obrigado por usar nosso sistema, obrigado!')
""" else:
    print('Operação inválida, digite uma opção válida') """

print('*' * 50)
