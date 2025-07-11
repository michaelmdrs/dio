class Gato:
	def __init__(self, nome, cor, acordado=True):
		self.nome = nome
		self.cor = cor
		self.acordado = acordado

	def __del__(self):
		print('Removendo a instância da classe.')

	def mia(self):
		print('miau')

def criar_gatos():
	gatos = Gato('Siameses', 'Cinza e Marrom', False)
	print(gatos.nome)

gato_1 = Gato('Garfield', 'Amarelo')
gato_1.mia()

criar_gatos()

# del_ é uma palavra reservada que serve para força o __del__ em outro local do código