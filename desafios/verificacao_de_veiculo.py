def verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual):
    idade_carro = ano_atual - ano_fabricacao
    if idade_carro <= 10:
        return f'{modelo}: Apto'
    else:
        return f'{modelo} Nao Apto'


def main():
    modelo = input('Modelo: ')
    ano_fabricacao = int(input('Ano Fabricação: '))
    ano_atual = int(input('Ano Atual: '))

    resultado = verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual)
    print(resultado)


if __name__ == "__main__":
    main()
