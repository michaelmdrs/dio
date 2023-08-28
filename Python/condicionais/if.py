import time

saldo = 1000
saque = float(input('Informe o valor do saque R$: '))

if saldo >= saque:
    time.sleep(2)
    print('Contando cédulas')
    time.sleep(2)
    print('Realizando saque...')
    time.sleep(2)
    print('Saque realizado!')
else:
    print('Saldo insuficiente para saque.')
