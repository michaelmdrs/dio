import time

conta_normal = True
conta_universitaria = False

saldo = 2800
saque = int(input('Informe o valor do saque R$: '))
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        time.sleep(2)
        print('Contando cédulas...')
        time.sleep(2)
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        time.sleep(2)
        print('Contando cédulas...')
        time.sleep(2)
        print('Saque realizado usando limite do cheque especial')
    else:
        print('Saldo insuficiente para saque!')
elif conta_universitaria:
    if saldo >= saque:
        time.sleep(2)
        print('Contando cédulas...')
        time.sleep(2)
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente para saque.')
else:
    print("""Sistema não identificou seu tipo de conta,
favor entrar em contato com o seu gerente.""")
print('*' * 40)
