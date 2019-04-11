
from Arestas import *
from Vertices import *

class Grafo():

	def __init__(self, rotulo):
		self.__rotulo = rotulo
		self.__vertices = list()
		self.__arestas = list()

	def getRotulo(self):
		return self.__rotulo

	def setRotulo(self, rotulo):
		self.__rotulo = rotulo

	def criarVertice(self,nome):
		vertice = Vertices(nome)
		self.__vertices.append(vertice)

	def getVertices(self):
		return self.__vertices

	def inserirAresta(self,nome,custo,vertice1,vertice2):
		for i in self.__vertices:
			if i.getNome() == vertice1:
				aux = i
			elif i.getNome() == vertice2:
				aux1 = i
		aresta = Arestas(nome,custo,aux,aux1)
		self.__arestas.append(aresta)
		aux.setAdjacente(aux1)
		aux1.setAdjacente(aux)
		

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
	def BuscaEmLargura(self,vsaida,vertice):
		visitados = list()
		fila = list()
		fila.append(vsaida)
		visitados.append(vsaida)
		while len(visitados) != len(self.__vertices) or len(fila) != 0:
			for i in self.__vertices:
				print(fila.index(0))
				if i.getNome() == fila.__getitem__(0):
					aux = i.getLista()
					for j in aux:
						if j.getNome() == vertice:
							return j
						elif j.getNome() not in visitados:
							visitados.append(j.getNome())
							fila.append(j.getNome())
				break
			fila.pop(0)
		print('vertice não encontrado')
	def BuscaEmProfundidade(self,vsaida,vertice):
		visitados = list()
		pilha = list()
		cont = 0
		tamanho = len(self._arestas)
		continuar = True
		visitados.append(vsaida)
		pilha.append(vsaida)
		while len(visitados) != len(self.__vertices) or len(pilha) != 0:
			cont = 0
			continuar = True
			i = self.__arestas[0]
			aux = pilha(len(pilha-1))
			while cont < tamanho or continuar == True:
				while i.getVertice1().getNome() != pilha[aux] or i.getVertice2().getNome() != pilha[aux] or cont < tamanho-1:
					cont+=1
					i = self.__arestas[cont]
				if i.getVertice1().getNome() == pilha[aux]:
					if i.getVertice2().getNome() not in visitados:
						visitados.append(i.getVertice2().getNome())
						pilha.append(i.getVertice2().getNome())
						continuar = False
				elif i.getVertice2().getNome() == pilha[aux]:
					if i.getVertice1().getNome() not in visitados:
						visitados.append(i.getVertice1().getNome())
						pilha.append(i.getVertice1().getNome())
						continuar = False
				elif cont >= tamanho :
					pilha.pop(len(pilha)-1)
				cont+=1
			if visitados[len(visitados)-1] == vertice:
				if i.getVertice1().getNome() == vertice:
					return i.getVertice1()
				else: return i.getVertice2()
		print('vertice não encontrado')

	def GerarArvoreMinima(self,vsaida):
		arvore = Grafo('Arvore Minima')
		arvore.criaVertice(vsaida)
		aresta= self._aresta[0]
		menor = 99999999999999999999999999999
		aux = arvore.getVertices()
		while len(aux) < len(self.__vertices):
			tamanho = aux[len(aux)]
			for j in aux:
				for i in self.__arestas:
					if i.getVertice1().getNome() == j.getNome() or i.getVertice2().getNome() == j.getNome():
						if i.getVertice1() not in aux or i.getVertice2() not in aux:
							if i.getCusto() < menor:
								menor = i.getCusto()
								aresta = i
			if aresta.getVertice1() not in aux:
				arvore.criaVertice(aresta.getVertice1().getNome())
			else: arvore.criaVertice(aresta.getVertice2().getNome())
			arvore.inserirAresta(aresta.getNome(), aresta.getCusto(), aresta.getVertice1().getNome(), aresta.getVertice2().getNome())
			aux = arvore.getVertices()
			menor = 99999999999999999999999999999
		return arvore




