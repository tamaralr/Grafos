from Tela import *

class Grafo():

	def __init__(self, rotulo, arestas, vertices):
		self._v = list()
		self._a = list()
		self.__rotulo = rotulo
		self.__arestas = arestas
		self.__vertices = vertices
		self.createGrafo()

	def getRotulo(self):
		return self.__rotulo

	def setRotulo(self, rotulo):
		self.__rotulo = rotulo

	def getArestas(self):
		return self.__arestas 

	def setArestas(self, arestas):
		self.__arestas = arestas

	def getVertices(self):
		return self.__vertices

	def setVertices(self, vertices):
		self.__vertices = vertices

	def createGrafo(self):
		qtdeVertices = self.getVertices()
		qtdeArestas = self.getArestas()
		
		for i in range(0,qtdeVertices):
			self.v.append(Tela.show_dialog("Insere o vértice [%d]: " % (i+1)))
		
		s = "----"
		for i in range(0,qtdeArestas):
			self.a.append(s)

		#concatenar lista a + s nos impares
		#v1 --- v2 --- v3
		f = list()
		for i in range(0,qtdeArestas):
			f.append(v.__getitem__(i) + a.__getitem__(i))
		
		f.append(v.pop())
		concatenatedString = ''.join(f)
		print(concatenatedString)
		Tela.print(f)





