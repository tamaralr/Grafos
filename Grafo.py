from Tela import *
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
			l.append(aux2.getNome())
			concat = ''.join(l)
			print(concat)





