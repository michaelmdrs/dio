def sacar(valor):
    saldo = 500

    if saldo >= valor:
        valor_saque = saldo - valor
        print(f'Saldo atual R$: {valor_saque}')
    else:
        print('Saldo insuficiente para realizar saque.')


def depositar(valor):
    saldo = 500
    saldo += valor

    if valor > 0:
        print(f'Deposito realizado com sucesso!')
        print(f'Valor depositado: R$ {valor:.2f}')


depositar(2000)
#  sacar(1500)
