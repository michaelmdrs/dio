""" def contar_vogais(frase):
    vogais = 'AEIOU'
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
        return contador


frase = input('Digite uma frase: ').upper()
qtd_vogais = contar_vogais(frase)
print(f'Na frase localizamos: {qtd_vogais} vogal(is) : {frase}') """

frase = input('Digite uma frase: ')
vogais = 'AEIOU'

for letra in frase:
    if letra.upper() in vogais:
        print(f'Na frase existe as seguinte(s) vogal(is): {letra.upper()}')
print()

for numero in range(0, 50):
    print(numero)

print()

for numeros in range(0, 51, 5):
    print(numeros)
