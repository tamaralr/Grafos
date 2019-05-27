from pydot import Node

class Vertice():
	def __init__(self,nome):
		self.__vertice = Node(nome, style='filled', fillcolor='green')
		self.__nome = nome		
		self.__adjacentes = list()


	def add_adjacentes(self,vertice):
		if vertice not in self.__adjacentes:
			self.__adjacentes.append(vertice)
			self.__adjacentes.sort()

	def setAdjacente(self, adjacente):
		self.__adjacentes.append(adjacente)

	def getNome(self):
		return self.__nome

	def getLista(self):
		return self.__adjacentes

	def isAdjacente(self,nome):
		for i in self.__adjacentes:
			if i==nome:
				return True
		return False

	def getVertice(self):
		return self.__vertice




