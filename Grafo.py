
from Aresta import *
from Vertice import *
from Config import *
from pydot import Dot

class Grafo():

	def __init__(self, rotulo):
		self.__rotulo = rotulo
		self.__grafoTela = Dot(graph_type = 'graph')
		self.__vertices = list()
		self.__arestas = list()
		
	def getRotulo(self):
		return self.__rotulo

	def setRotulo(self, rotulo):
		self.__rotulo = rotulo

	def criarVertice(self,nome):
		vertice = Vertice(nome)
		self.__vertices.append(vertice)
		self.__grafoTela.add_node(vertice.getVertice())

	def criarVerticeComCoordenads(self,nome,cx,cy):
		vertice = Vertice(nome)
		vertice.InserirCoordenadas(cx, cy)
		self.__vertices.append(vertice)
		self.__grafoTela.add_node(vertice.getVertice())

	def getVertices(self):
		return self.__vertices

	def getArestas(self):
		return self.__arestas

	def inserirAresta(self,nome,custo,vertice1,vertice2):
		for i in self.__vertices:
			if i.getNome() == vertice1:
				aux = i
			elif i.getNome() == vertice2:
				aux1 = i

		aresta = Aresta(nome,custo,aux,aux1)
		aux.setAdjacente(aux1)
		aux1.setAdjacente(aux)
		self.__grafoTela.add_edge(aresta.getAresta())
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

	def removerAresta(self, nome):
		conta= 0
		for i in self.__arestas:
			if i.getNome() == nome:
				self.__arestas.pop(conta)
				break
			conta+=1

	def verificarAdjacente(self, vertice1, vertice2):
		for i in self.__vertices:
			if i.getNome() == vertice1:
				for j in i.getLista():
					if j.getNome() == vertice2:
						return True
			elif i.getNome() == vertice2:
				for j in i.getLista():
					if j.getNome() == vertice1:
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
		print(self.__rotulo)
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
		self.__grafoTela.write_png(Config.DIRETORIO_PADRAO_IMAGEM)

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


	def grafoConvexoEhPlanar(self):
		qtdeArestas = len(self.__arestas)
		qtdeVertices = len(self.__vertices)
		total = 0
		print("Vertices: ",qtdeVertices)
		print("Arestas: ",qtdeArestas)
		if(qtdeVertices<3):
			return True

		if qtdeVertices >= 3:
			total = 3 * qtdeVertices - 6
			print("Total: ", total)
			if(not qtdeArestas <= total):
				print("condicao1")
				return False

			if not self.temCiclosDeComprimentoTres():
				total = 2 * qtdeVertices - 4
				print("Total: ", total)
				if not qtdeArestas <= total:
					print("condicao2")
					return False

			return True
		else:
			return False	

	def temCiclosDeComprimentoTres(self):			
		for vertice in self.__vertices:
			for adjacente in vertice.getLista():
				for adjacenteRetorno in adjacente.getLista():			
					if self.verificarAdjacente(vertice.getNome(), adjacenteRetorno.getNome()):
						return True
		return False
	def coloreVertices(self):
		#azul-claro rosa verde marrom
		cores = list();
		#"#00c6c5", "#cc0132", "#538e6d", "#843907"
		cores.append("#00c6c5")
		cores.append("#cc0132")
		cores.append("#538e6d")
		cores.append("#843907")

		pos = 0
		for vertice in self.__vertices:

			vertice.setVertice(cores[pos])
			pos += 1 
			for adjacente in vertice.getLista():
				for adjacenteDoAdjacente in adjacente.getLista():
					vertice.setVertice(cores[pos])
					pos += 1
					if pos >= 4:
						pos = 0

	def Dijkstra(self,vsaida,vchegada):
		fechados = list()
		estimativa = list()
		precedente = list()
		listaVertices = list()
		menor = -1
		selecionado = ""
		contador = len(self.__vertices)
		for i in self.__vertices:
			listaVertices.append(i.getNome())
			if(i.getNome() == vsaida):
				estimativa.append(0)
			else:
				estimativa.append(-1)
		for j in range(contador):
			for i in range(contador):
				if (listaVertices[i] not in fechados):
					if(menor == -1):
						menor = estimativa[i]
						selecionado = listaVertices[i]
					elif (estimativa[i] < menor):
						menor = estimativa[i]
						selecionado = listaVertices[i]
			fechados.append(selecionado)
			for k in self.__arestas:
				if(k.getVertice1().getNome() not in fechados and k.getVertice2().getNome() == selecionado ):
					custo = k.getCusto()
					indexAdjacente = listaVertices.index(k.getVertice1().getNome())
					indexAtual = listaVertices.index(selecionado)
					if(estimativa[indexAdjacente]== -1):
						estimativa[indexAdjacente]== custo
						precedente[indexAdjacente]== selecionado
					else:
						custo = custo + estimativa[indexAtual]
						if(custo < estimativa[indexAdjacente]):
							estimativa[indexAdjacente] = custo
							precedente[indexAdjacente] = selecionado
				elif(k.getVertice1().getNome() == selecionado and k.getVertice2().getNome() not in fechados):
					custo = k.getCusto()
					indexAdjacente = listaVertices.index(k.getVertice2().getNome())
					indexAtual = listaVertices.index(selecionado)
					if(estimativa[indexAdjacente]== -1):
						estimativa[indexAdjacente]== custo
						precedente[indexAdjacente]== selecionado
					else:
						custo = custo + estimativa[indexAtual]
						if(custo < estimativa[indexAdjacente]):
							estimativa[indexAdjacente] = custo
							precedente[indexAdjacente] = selecionado

	def AEstrela(self,vsaida,vchegada):
		distanciaLinhaReta = list()
		ordemLista = list()
		cobjetivo = list()
		proximo = vsaida
		aproximacoes = list()
		nodos = list()
		calculoDeslocamento = list
		distancia = 0
		continua = True
		grafo = Grafo('A*')
		for i in self.__vertices:
			if( i.getNome() == vchegada):
				aux = i.getCoordenadas()
				cobjetivo.append(aux[0])
				cobjetivo.append(aux[1])
		for i in self.__vertices:
			aux = i.getCoordenadas()
			distancia = abs(cobjetivo[0] - aux[0]) + abs(cobjetivo[1] - aux[1])
			distanciaLinhaReta.append(distancia)
			ordemCidadesLista.append(i.getNome())
		grafo.criarVertice(proximo)
		while(continua):
			for i in self._arestas:
				if(i.getVertice1().getNome() == proximo):
					aproximacoes.append(i.getCusto())
					nodos.append(i.getVertice2().getNome())
				elif( i.getVertice2().getNome() == proximo ):
					aproximacoes.append(i.getCusto())
					nodos.append(i.getVertice1().getNome())
			contador = len(aproximacoes)
			for i in range(contador):
				index = ordemLista.index(nodos[i])
				aux = distancia + aproximacoes[i] + distanciaLinhaReta[index]
				calculoDeslocamento.append(aux)
			aux = min(calculoDeslocamento)
			index = calculoDeslocamento.index(aux)
			grafo.criarVertice(nodos[index])
			grafo.inserirAresta('------', aproximacoes[index], proximo, nodos[index])
			distancia = distancia + aproximacoes[index]
			proximo = nodos[index]
			if(proximo == vchegada):
				continua = False









	

