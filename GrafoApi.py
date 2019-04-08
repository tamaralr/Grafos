from Grafo import *
from Tela import *

class GrafoApi():

	@staticmethod
	def main():
		grafo = Grafo("grafo01")
		grafo.criarVertice("v1")
		grafo.criarVertice("v2")
		grafo.criarVertice("v3")
		grafo.inserirAresta("---1---",10,'v1','v3')
		grafo.exibirGrafo()
		grafo.removerVertice('v3')
		print('removi')
		grafo.exibirGrafo()

if __name__ ==  '__main__':
	#execução pelo terminal
	GrafoApi.main()
	print("executado pelo terminal")
else:
	#execução pelo módulo
	GrafoApi.main()
	print("executado pelo modulo")