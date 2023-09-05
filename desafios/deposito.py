valor = float(input('Insira o valor do depósito R$: '))

if valor > 0:
    print('Deposito realizado com sucesso!')
    print(f'Saldo atual: R$ {valor:.2f}')
elif valor == 0:
    print('Encerrando o programa...')
else:
    print('Valor invalido! Digite um valor maior que zero.')
