saldo_total = int(input('Digite o valor do seu saldo R$: '))
valor_saque = int(input('Digite o valor do seu saque R$: '))

saldo_disponivel = saldo_total
saldo_atual = saldo_disponivel - valor_saque

if saldo_disponivel >= valor_saque:
    print(f'Saque realizado com sucesso! Novo saldo: {saldo_atual}')
else:
    print('Saldo insuficiente. Saque nao realizado!')
