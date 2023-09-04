saldo_atual = float(input('Digite o saldo atual R$: '))
valor_deposito = float(input('Digite o valor do deposito R$: '))
valor_retirada = float(input('Digite o valor da saque R$: '))


def saldo_atualizado():
    transacao = saldo_atual + valor_deposito
    return transacao - valor_retirada


print(f'Saldo atualizado na conta R$: {saldo_atualizado()}')
