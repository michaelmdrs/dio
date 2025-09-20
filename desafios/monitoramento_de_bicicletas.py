class BicicletaInterna:
    def __init__(self, modelo, nivel_bateria):
        self.modelo = modelo
        self.nivel_bateria = nivel_bateria

    def calcular_distancia(self):
        # TODO: calculate a distance between with base to nivel of battery
        distancia_percorrrida = self.nivel_bateria * 0.5
        return distancia_percorrrida

    def obter_mensagem(self):
        # TODO: return message formatted with model and distance
        distancia_estimada = self.calcular_distancia()
        return f'{self.modelo}: Distancia estimada = {distancia_estimada:.1f} km'


def main():
    modelo = input('Modelo: ')
    nivel_str = input('Nível Bateria: ')
    nivel_bateria = int(nivel_str)

    # TODO: create a object BicicleInternal with data read
    bicicleta = BicicletaInterna(modelo, nivel_bateria)
    print(bicicleta.obter_mensagem())


if __name__ == '__main__':
    main()
