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
		if grafo2.grafoConvexoEhPlanar():
			y= "O Grafo é Planar!" 
		else: 
			y="O Grafo não é Planar!"
	
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

		grafo3 = Grafo("Exemplo A* ")
		grafo3.criarVerticeComCoordenadas('A',950,231)
		grafo3.criarVerticeComCoordenadas('B',607,486)
		grafo3.criarVerticeComCoordenadas('C',891,762)
		grafo3.criarVerticeComCoordenadas('D',456,19)
		grafo3.criarVerticeComCoordenadas('E',821,445)
		grafo3.criarVerticeComCoordenadas('F',615,792)
		grafo3.criarVerticeComCoordenadas('G',922,738)
		grafo3.criarVerticeComCoordenadas('H',176,406)
		grafo3.criarVerticeComCoordenadas('I',935,917)
		grafo3.criarVerticeComCoordenadas('J',410,894)
		grafo3.criarVerticeComCoordenadas('K',58,353)
		grafo3.criarVerticeComCoordenadas('L',813,10)
		grafo3.criarVerticeComCoordenadas('M',139,203)
		grafo3.criarVerticeComCoordenadas('N',199,604)
		grafo3.criarVerticeComCoordenadas('O',272,199)
		grafo3.criarVerticeComCoordenadas('P',15,747)
		grafo3.criarVerticeComCoordenadas('Q',445,932)
		grafo3.criarVerticeComCoordenadas('R',466,419)
		grafo3.criarVerticeComCoordenadas('S',846,525)
		grafo3.criarVerticeComCoordenadas('T',203,672)
		grafo3.inserirAresta('------',1,'A','E')
		grafo3.inserirAresta('------',1,'A','S')
		grafo3.inserirAresta('------',1,'A','G')
		grafo3.inserirAresta('------',1,'A','L')
		grafo3.inserirAresta('------',1,'A','B')
		grafo3.inserirAresta('------',1,'B','J')
		grafo3.inserirAresta('------',1,'B','F')
		grafo3.inserirAresta('------',1,'B','R')
		grafo3.inserirAresta('------',1,'B','T')
		grafo3.inserirAresta('------',1,'B','S')
		grafo3.inserirAresta('------',1,'B','E')
		grafo3.inserirAresta('------',1,'C','I')
		grafo3.inserirAresta('------',1,'C','G')
		grafo3.inserirAresta('------',1,'D','L')
		grafo3.inserirAresta('------',1,'D','M')
		grafo3.inserirAresta('------',1,'D','R')
		grafo3.inserirAresta('------',1,'F','J')
		grafo3.inserirAresta('------',1,'F','S')
		grafo3.inserirAresta('------',1,'G','I')
		grafo3.inserirAresta('------',1,'H','P')
		grafo3.inserirAresta('------',1,'H','O')
		grafo3.inserirAresta('------',1,'H','N')
		grafo3.inserirAresta('------',1,'I','Q')
		grafo3.inserirAresta('------',1,'J','Q')
		grafo3.inserirAresta('------',1,'J','P')
		grafo3.inserirAresta('------',1,'K','M')
		grafo3.inserirAresta('------',1,'K','P')
		grafo3.inserirAresta('------',1,'L','R')
		grafo3.inserirAresta('------',1,'M','O')
		grafo3.inserirAresta('------',1,'N','R')
		grafo3.inserirAresta('------',1,'N','T')
		grafo3.inserirAresta('------',1,'N','P')
		grafo3.inserirAresta('------',1,'O','R')
		grafo3.inserirAresta('------',1,'P','T')
		grafo3.AEstrela('A','N')

		grafo4 = Grafo("Exemplo Dijkstra")
		grafo4.criarVertice('A')
		grafo4.criarVertice('B')
		grafo4.criarVertice('C')
		grafo4.criarVertice('D')
		grafo4.criarVertice('E')
		grafo4.criarVertice('F')
		grafo4.inserirAresta('------', 4,'A','B')
		grafo4.inserirAresta('------', 2,'A','C')
		grafo4.inserirAresta('------', 1,'B','C')
		grafo4.inserirAresta('------', 5,'B','D')
		grafo4.inserirAresta('------', 8,'C','D')
		grafo4.inserirAresta('------', 10,'C','E')
		grafo4.inserirAresta('------', 2,'D','E')
		grafo4.inserirAresta('------', 6,'D','F')
		grafo4.inserirAresta('------', 2,'E','F')
		grafo4.Dijkstra('A', 'E')

if __name__ ==  '__main__':
	#execução pelo terminal
	GrafoApi.main()
	print("executado pelo terminal")
else:
	#execução pelo módulo
	GrafoApi.main()
	print("executado pelo modulo")