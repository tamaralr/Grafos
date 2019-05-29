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
		grafo = Grafo('Grafok5')
		grafo.criarVertice('V1')
		grafo.criarVertice('V2')
		grafo.criarVertice('V3')
		grafo.criarVertice('V4')
		grafo.criarVertice('V5')

		grafo.inserirAresta('---A1---',20,'V1','V2')
		grafo.inserirAresta('---A2---',40,'V1','V5')
		grafo.inserirAresta('---A3---',10,'V1','V3')
		grafo.inserirAresta('---A4---',30,'V1','V4')

		grafo.inserirAresta('---A5---',40,'V2','V5')

		grafo.inserirAresta('---A6---',40,'V2','V3')
		grafo.inserirAresta('---A7---',40,'V5','V3')
		grafo.inserirAresta('---A8---',40,'V4','V3')

		grafo.inserirAresta('---A9---',40,'V4','V2')
		grafo.inserirAresta('---A10---',40,'V4','V5')

		r = ""
		if grafo.grafoConexoEhPlanar():
			r= "O Grafo é Planar!\n" 
		else: 
			r="O Grafo não é Planar!\n"

		print(r)
		grafo2 = Grafo("Grafo k(3,3)")
		grafo2.criarVertice('V1')
		grafo2.criarVertice('V2')
		grafo2.criarVertice('V3')
		grafo2.criarVertice('V4')
		grafo2.criarVertice('V5')
		grafo2.criarVertice('V6')

		grafo2.inserirAresta('---A1---',10,'V1','V4')
		grafo2.inserirAresta('---A2---',30,'V1','V5')
		grafo2.inserirAresta('---A3---',20,'V1','V6')

		grafo2.inserirAresta('---A4---',40,'V2','V4')
		grafo2.inserirAresta('---A5---',40,'V2','V5')
		grafo2.inserirAresta('---A6---',40,'V2','V6')

		grafo2.inserirAresta('---A7---',40,'V3','V4')
		grafo2.inserirAresta('---A8---',40,'V3','V5')
		grafo2.inserirAresta('---A9---',40,'V4','V6')

		grafo2.exibirGrafo()

		y = ""
		if grafo2.grafoConexoEhPlanar():
			y= "O Grafo é Planar!\n" 
		else: 
			y="O Grafo não é Planar!\n"

		# a=grafo.pegarCustoAresta('---1---')
		# print(a)
		# b=grafo.retornarExtremosAresta('---4---')
		# for i in b:
		# 	print(i.getNome())
		# # grafo.removerVertice('c')
		# grafo.removerAresta('---1---')
		# grafo.exibirGrafo()
		#c=grafo.BuscaEmLargura('a', 'd')
		#print('BuscaEmLargura V1: ',c.getNome())
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