from Grafo import *
from Tela import *

class GrafoApi():

	@staticmethod
	def main():
		# necessario retorna um lista com os 3 parametros
		#lista = Tela.input_grafo("Nome do Grafo: ","qtde arestas", "qtde vértices")
		#grafo = Grafo("Grafo1", 2, 3)
		#grafo = Grafo(lista[0], lista[1], lista[2])


if __name__ ==  '__main__':
	#execução pelo terminal
	GrafoApi.main()
	print("executado pelo terminal")
else:
	#execução pelo módulo
	GrafoApi.main()
	print("executado pelo modulo")