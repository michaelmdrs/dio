MAIOR_IDADE = 18

IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Usuário com idade permitida.')
elif idade >= IDADE_ESPECIAL and idade < MAIOR_IDADE:
    print('Usuário liberado para as aulas teóricas, mas não pode fazer as aulas práticas.')
else:
    print('Usuário não tem idade permitida para prosseguir.')
