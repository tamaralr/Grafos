
from Aresta import *
from Vertice import *
from Config import *
from pydot import Dot

class Grafo():

	def __init__(self, rotulo):
		self.__rotulo = rotulo
		self.grafoTela = Dot(graph_type = 'graph')
		self.__vertices = list()
		self.__arestas = list()
		
	def getRotulo(self):
		return self.__rotulo

	def setRotulo(self, rotulo):
		self.__rotulo = rotulo

	def criarVertice(self,nome):
		vertice = Vertice(nome)
		self.__vertices.append(vertice)
		print(vertice.getVertice())
		self.grafoTela.add_node(vertice.getVertice())


	def getVertices(self):
		return self.__vertices

	def inserirAresta(self,nome,custo,vertice1,vertice2):
		for i in self.__vertices:
			if i.getNome() == vertice1:
				aux = i
			elif i.getNome() == vertice2:
				aux1 = i

		aresta = Aresta(nome,custo,aux,aux1)
		print("aresta:" + aresta.getNome())
		aux.setAdjacente(aux1)
		aux1.setAdjacente(aux)
		self.grafoTela.add_edge(aresta.getAresta())
		self.__arestas.append(aresta)		

	def removerVertice(self,vertice):
		conta = 0
		for i in self.__arestas:
			if i.getVertice1().getNome()== vertice:
				aux = i.getVertice2()
				contv = 0
				for j in aux.getLista():
					if j.getNome() == vertice:
						aux.getLista().pop(contv)
				contv+=1
				self.__arestas.pop(conta)
			elif i.getVertice2().getNome()== vertice:
				aux = i.getVertice1()
				contv = 0
				for j in aux.getLista():
					if j.getNome() == vertice:
						aux.getLista().pop(contv)
					contv+=1
				self.__arestas.pop(conta)
			conta+=1
		conta = 0
		for i in self.__vertices:
			if i.getNome() == vertice:
				self.__vertices.pop(conta)
				break
			conta+=1

	def removerAresta(self,nome):
		conta= 0
		for i in self.__arestas:
			if i.getNome() == nome:
				self.__arestas.pop(conta)
				break
			conta+=1

	def verificarAdjacente(self,vertice1,vertice2):
		for i in self.__vertices:
			if i.getNome() == vertice1:
				for j in i.getLista():
					if j.getNome == vertice2:
						return True
			elif i.getNome() == vertice2:
				for j in i.getLista():
					if j.getNome == vertice1:
						return True
		return False
	def pegarCustoAresta(self,nome):
		for i in self.__arestas:
			if i.getNome() == nome:
				return i.getCusto()

	def retornarExtremosAresta(self,nome):
		for i in self.__arestas:
			if i.getNome() == nome:
				return i.getVertices()

	def exibirGrafo(self):
		l =[]

		for i in self.__arestas:
			l= i.getVertices()
			aux2 = l.pop()
			aux1 = l.pop()
			l.append(aux1.getNome())
			l.append(i.getNome())
			l.append(str(i.getCusto()))
			l.append(aux2.getNome())
			concat = ''.join(l)
			print(concat)

				
	def showGrafoTela(self):
		l = []

		for i in self.__arestas:
			l = i.getVertices()
			aux2 = l.pop()
			aux1 = l.pop()
			l.append(aux1.getNome())
			l.append(i.getNome())
			l.append(str(i.getCusto()))
			l.append(aux2.getNome())
			concat = ''.join(l)
			print(concat)
	
	def carregarImagem(self):
		self.grafoTela.write_png(Config.DIRETORIO_PADRAO_IMAGEM)

	def BuscaEmLargura(self,vsaida,vertice):
		visitados = list()
		fila = list()
		fila.append(vsaida)
		visitados.append(vsaida)
		while len(visitados) != len(self.__vertices) or len(fila) != 0:
			print(len(fila))
			for i in self.__vertices:
				if i.getNome() == fila[0]:
					aux = i.getLista()
					for j in aux:
						if j.getNome() == vertice:
							return j
						elif j.getNome() not in visitados:
							visitados.append(j.getNome())
							fila.append(j.getNome())
			fila.pop(0)
		print('vertice não encontrado')
	def BuscaEmProfundidade(self,vsaida,vertice):
		visitados = list()
		pilha = list()
		cont = 0
		tamanho = len(self.__arestas)
		continuar = True
		visitados.append(vsaida)
		pilha.append(vsaida)
		while len(visitados) != len(self.__vertices) or len(pilha) != 0:
			cont = 0
			continuar = True
			i = self.__arestas[0]
			while cont < tamanho and continuar == True:
				while(i.getVertice1().getNome() != pilha[-1]) and (i.getVertice2().getNome() != pilha[-1]):
					if cont>=(tamanho -1):
						break
					else:
						i = self.__arestas[cont]
						cont+=1
				cont+=1
				if i.getVertice1().getNome() == pilha[-1]:
					if i.getVertice2().getNome() not in visitados:
						visitados.append(i.getVertice2().getNome())
						pilha.append(i.getVertice2().getNome())
						continuar = False
					else:
						i= self.__arestas[cont]
				elif i.getVertice2().getNome() == pilha[-1]:
					if i.getVertice1().getNome() not in visitados:
						visitados.append(i.getVertice1().getNome())
						pilha.append(i.getVertice1().getNome())
						continuar = False
					else:
						i= self.__arestas[cont]
				elif cont >= tamanho :
					continuar = False
					pilha.pop(len(pilha)-1)
			if visitados[-1] == vertice:
				if i.getVertice1().getNome() == vertice:
					return i.getVertice1()
				else: return i.getVertice2()
		print('vertice não encontrado')

	def GerarArvoreMinima(self,vsaida):
		arvore = Grafo('Arvore Minima')
		arvore.criarVertice(vsaida)
		aresta= self.__arestas[0]
		menor = None
		aux = arvore.getVertices()
		verticev = []
		verticev.append(aux[len(aux)-1].getNome())
		while len(aux) < len(self.__vertices):
			for j in aux:
				for i in self.__arestas:
					if i.getVertice1().getNome() == j.getNome() or i.getVertice2().getNome() == j.getNome():
						if i.getVertice1().getNome() not in verticev or i.getVertice2().getNome() not in verticev:
							if menor == None:
								menor = i.getCusto()
								aresta = i
							elif i.getCusto() < menor:
								menor = i.getCusto()
								aresta = i
			if aresta.getVertice1().getNome() not in verticev:
				print('if vertice 1')
				arvore.criarVertice(aresta.getVertice1().getNome())
			else: 
				print('if vertice 2')
				arvore.criarVertice(aresta.getVertice2().getNome())
			aux = arvore.getVertices()
			verticev.append(aux[len(aux)-1])
			arvore.inserirAresta(aresta.getNome(), aresta.getCusto(), aresta.getVertice1().getNome(), aresta.getVertice2().getNome())	
			menor = None
		return arvore




