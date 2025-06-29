# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input('Valor do produto R$: ').strip())
cupom = input('Digite o cupom: ').strip().upper()
# TODO: Aplique o desconto se o cupom for válido:
if cupom == "DESCONTO10":
    cupom_10 = preco * descontos["DESCONTO10"]
    desconto_10 = preco - cupom_10
    print(f"Desconto aplicado R$: {desconto_10}")
elif cupom == "DESCONTO20":
    cupom_20 = preco * descontos["DESCONTO20"]
    desconto_20 = preco - cupom_20
    print(f"Desconto aplicado R$: {desconto_20:.2f}")
elif cupom == "SEM_DESCONTO":
    print(preco)
else:
    print("Cupom inválido")
# Exibir o preço final