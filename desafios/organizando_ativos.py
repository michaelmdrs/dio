ativos = []

quantidade_ativos = int(input('Digite a quantidade de ativos: '))


for _ in range(quantidade_ativos):
    codigo_ativo = input('Digite seus ativos: ')
    ativos.append(codigo_ativo)


ordem_ativos = sorted(ativos)

[print(ativo) for ativo in ordem_ativos]

# listagem_ativos = [print(ordem_ativos) for ordem_ativos in ativos]


#  print(f'Lista de Ativos: {ordem_ativos}\n')
