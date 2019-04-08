class Arestas():
	def __init__(self, nome, custo, vertice1,vertice2):
		self.__nome = nome
		self.__custo = custo
		self.__vertice1 = vertice1
		self.__vertice2 = vertice2


	def setNome(self, nome):
		self.__nome = nome

	def setCusto(self, custo):
		self.__custo = custo

	def getNome(self):
		return self.__nome

	def getCusto(self):
		return self.__custo

	def getVertice1(self):
		return self.__vertice1
		
	def getVertice2(self):
		return self.__vertice2

	def getVertices(self):
		return [self.__vertice1,self.__vertice2]



