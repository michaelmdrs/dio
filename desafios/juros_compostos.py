valor_inicial = float(input('Digite o valor inicial R$: '))
taxa_juros = float(input('Digite a taxa de juros em %: '))
periodo = int(input('Quantos anos deseja investir: '))


def calcular_juros_compostos(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    return round(valor_final, 2)


resultado = calcular_juros_compostos(valor_inicial, taxa_juros, periodo)
print("Valor Final:", resultado)
