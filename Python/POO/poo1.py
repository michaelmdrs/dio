class Cachorro:
	def __init__(self, nome, cor, acordado=True):
		self.nome = nome
		self.cor = cor
		self.acordado = acordado

	def latir(self):
		print('Auauau')


	def dormir(self):
		self.acordado = False
		print('ZZzzzzz...')


cao_1 = Cachorro('Chappie', 'Caramelo', False)
cao_2 = Cachorro('Aladim', 'Preto e Branco')

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)