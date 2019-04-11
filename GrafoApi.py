from Grafo import *
from Tela import *


class GrafoApi():

	@staticmethod
	def main():
# 		while True:
# 			n = input("Digite um numero para operação")
# 			print("1 - Inseri aresta")
# 			print("2 - Remover aresta")
# 			print("3 - Inseri Vértice")
# 			print("4 - Remover Vértice")
# 			print("5 - PRIM")
# 			print("6 - Profundidade")
# 			print("7 - Largura")

# 			grafo = Grafo("grafo01")

# 			c = input("Digite um numero para operação")
# 		    if c==1:
# 		    	v1 = input(str("Nome vértice 1: "))
# 		    	v2 = input(str("Nome vértice 2: "))
# 		    	for a in grafo.getVertices()
# 		    	nomeA = input(str("Digite nome aresta"))
# 		        grafo.inserirAresta(nomeA,10,'v1','v3')
# 		    if c==2:
# 		        print getpass.getuser()
# 		    if c==3:
# 		        print date.today()
# 		    if c==4:
# 		        quit()
# 		    else:
# 		        print "opção inexistente"
		grafo = Grafo('Grafo01')
		grafo.criarVertice('a')
		grafo.criarVertice('b')
		grafo.criarVertice('c')
		grafo.criarVertice('d')
		grafo.inserirAresta('---1---',10,'a','b')
		grafo.inserirAresta('---2---',20,'a','c')
		grafo.inserirAresta('---3---',30,'b','c')
		grafo.inserirAresta('---4---',40,'c','d')
		grafo.exibirGrafo()
		# if grafo.verificarAdjacente('b','d') ==True:
		# 	print('é adjascente')
		# else: 
		# 	print('não é adjascente')
		# a=grafo.pegarCustoAresta('---1---')
		# print(a)
		# b=grafo.retornarExtremosAresta('---4---')
		# for i in b:
		# 	print(i.getNome())
		# # grafo.removerVertice('c')
		# grafo.removerAresta('---1---')
		# grafo.exibirGrafo()
		c=grafo.BuscaEmLargura('a', 'd')
		print('BuscaEmLargura V1: ',c.getNome())
		# d=grafo.BuscaEmProfundidade('a', 'd')
		# print('BuscaEmProfundidade V2: ',d.getNome())




if __name__ ==  '__main__':
	#execução pelo terminal
	GrafoApi.main()
	print("executado pelo terminal")
else:
	#execução pelo módulo
	GrafoApi.main()
	print("executado pelo modulo")