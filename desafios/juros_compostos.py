valor_inicial = float(input('Digite o valor inicial R$: '))
taxa_juros = float(input('Digite a taxa de juros em %: '))
periodo = int(input('Quantos anos deseja investir: '))

valor_final = valor_inicial

for ano in range(periodo):
    valor_final *= (1 + taxa_juros)

print(f"Valor final do investimento: R$ {valor_final:.2f}")

""" def calcular_juros_compostos(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    return round(valor_final, 2)


resultado = calcular_juros_compostos(valor_inicial, taxa_juros, periodo)
print("Valor Final:", resultado) """


