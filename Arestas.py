class Arestas():
	def __init__(self, nome, custo, vertice):
		self.__nome = nome
		self.__custo = custo
		self.__vertice = vertice


	def setNome(self, nome):
		self.__nome = nome

	def setCusto(self, custo):
		self.__custo = custo

	def setVertice(self, vertice):
		self.__vertice = vertice


	def getNome(self):
		return self.__nome

	def getCusto(self):
		return self.__custo

	def getVertice(self):
		return self.__vertice



