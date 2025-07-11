class Bicicleta():
	"""docstring for ClassName"""
	def __init__(self, cor, modelo, ano, valor, nro_marcha, marcha):
		self.cor = cor
		self.modelo = modelo
		self.ano = ano
		self.valor = valor
		self.nro_marcha = nro_marcha
		self.marcha = marcha

	def buzinar(self):
		print('Biiip, biiip')

	def parar(self):
		print('Parou de pedalar, bicicleta está parada.')

	def correr(self):
		print('Você está correndo, Vruummmmmm...')

	def trocar_marcha(self, nro_marcha):
		print('Trocando marcha')

		def _troca_marcha_():
			if nro_marcha > self.marcha:
				print('Marcha trocada')

			else:
				print('Não é possível trocar de marcha')


	'''def __str__(self):
		return f'Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}'''

	def __str__(self):
		return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta('Preta', 'Caloi', 2023, 950, 21, 18)
# print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)
# caloi.correr()
# caloi.parar()

monark = Bicicleta('Vermelha', 'monark', 2002, 450, 18, 25)
print(monark.modelo, monark.ano)
monark.buzinar()

print(monark)