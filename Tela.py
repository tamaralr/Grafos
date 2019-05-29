from tkinter import * 
from tkinter import messagebox 
from functools import partial
from PIL import ImageTk, Image
import ImagemUtil
from ImagemUtil import *
from Config import *
from TelaUtil import *
from Grafo import *


QTDE_VERTICE = 0
FRAMES = []
NOME_ARESTA = 0
NOME_VERTICE = 0
ATUALIZACAO_TELA = 0
class TelaPrincipal:

    def incrementaAtualizacao(self): 
        global ATUALIZACAO_TELA
        ATUALIZACAO_TELA = ATUALIZACAO_TELA + 1

    def getAtualizacao(self):
        return ATUALIZACAO_TELA

    def center(self, window): 
        #win.geometry("1364x731+0+0") #1364x731
        window.update_idletasks()       
        width_tk = window.winfo_width()
        height_tk = window.winfo_height()
        width_tela = window.winfo_screenwidth()
        height_tela = window.winfo_screenheight()
        x = (width_tela - width_tk) // 2
        y = (height_tela - height_tk) // 2
        window.geometry('{}x{}+{}+{}'.format(width_tela, height_tela, x-9, y-9))

    def __init__(self):
        self.root = Tk()
        self.imagemBotaoAdd= PhotoImage(file="add-button.png")
        # flat, groove, raised, ridge, solid, or sunken
        self.painelRoot = PanedWindow(self.root, relief="sunken", border=2)
        self.painelRoot.grid(row=0, column=0, sticky='N', ipadx=0, ipady=0, padx=5)

        self.frameImagem = LabelFrame(self.painelRoot, text="Grafo", width=700, height=600)
        self.frameImagem.grid(row=1, column=0, sticky='NW', ipadx= 0, ipady=0, padx=10, pady=10)
        self.update_img_canvas = any    
        self.canvas = Canvas(self.frameImagem, width=700, height=600, bg="white", borderwidth=2, highlightthickness=2, scrollregion=(0,0,800,700))
        self.fileImagem = any
        self.criaCanvas()

        self.secundario = PanedWindow(self.root, relief="sunken", border=1)
        self.secundario.grid(row=0, column=1, sticky='N', ipadx=0, ipady=10, padx=20, pady=30)

        self.opcoesTela = LabelFrame(self.secundario, text= "Opções de Tela: ")
        self.opcoesTela.grid(row=1,column=1, stick="N", ipadx= 0, ipady=0, padx=30,pady=10)

        self.frameVertice = Frame(self.opcoesTela)
        self.frameVertice.grid(row=2, column=0, stick="W", padx=0,pady=5, ipadx=0)

        self.grafo = Grafo("Grafo")
        self.criaVertice()

        self.frameAresta = Frame(self.opcoesTela)
        self.frameAresta.grid(row=3, column=0, stick="W", padx=0,pady=20, ipadx=0)
        self.string_vars = []
        self.values = ["","","",""]
        self.dados_aresta = ("Nome", "Custo", "VerticeA", "VerticeB")
        self.criaArestas() 

        self.frameBotoes = LabelFrame(self.secundario, text="Escolha opação para gerar o Grafo: ")
        self.frameBotoes.grid(row=2, column=1, padx=30, pady=10, stick= "N")
        self.btnGerarGrafo = any
        self.btnGerarGrafoBuscaLargura = any
        self.btnGerarGrafoBuscaProfundidade = any
        self.btnGerarGrafoPrim = any
        self.btnVerificarGrafoPlanar = any
        self.criarBotoesMetodosGrafo()


    def preencheDadosAresta(self):
        for f in self.dados_aresta:
            i = len(self.string_vars)
            self.string_vars.append(StringVar())
            self.string_vars[i].trace("w", lambda name, index, mode, var=self.string_vars[i], i=i: self.entryupdate(var, i))
            Label(self.frameAresta, text=f).grid(column=0, row=i+1, stick="w", padx=15)
            Entry(self.frameAresta, width=6, textvariable=self.string_vars[i]).grid(column=1, row=i+1,stick="W", padx=15)
    
    def entryupdate(self, sv, i):
        bAresta = Button(self.frameAresta, relief="groove", border=3, command=self.addAresta)
        bAresta.config(image=self.imagemBotaoAdd, height=26, width=36)
        bAresta.grid(row=1, column=2, padx=15, pady=10, stick="W")

        if(i == 0):
            self.values[0] = sv.get()

        if(i == 1):
            self.values[1] = sv.get()

        if(i == 2):
            self.values[2] = sv.get()

        if(i == 3):
            self.values[3] = sv.get()


    def criaArestas(self):
        Label(self.frameAresta, text="Add Arestas: ").grid(row=0, column=0, stick="W")
        self.preencheDadosAresta()

    def addAresta(self):
        print("Nome: %s" % self.values[0])
        print("Custo: %s" % self.values[1])
        print("VA: %s" % self.values[2])
        print("VB: %s" % self.values[3])
        self.grafo.inserirAresta(self.values[0], self.values[1], self.values[2], self.values[3])
        self.atualizaTela()

    def criaVertice(self):
        Label(self.frameVertice, text="Add Vertice: ").grid(row=0, column=0, stick="W")
        Label(self.frameVertice, text="Nome: ").grid(row=1, column=0, stick="W", padx=15)
        varNome = StringVar()
        e = Entry(self.frameVertice, width=6, textvariable=varNome)
        e.grid(row=1, column=1, stick="W", padx=15)
        varNome.set("V%s" % NOME_VERTICE)

        bVertice = Button(self.frameVertice, relief="groove", border=3, command=partial(self.addVertice, e, varNome))
        bVertice.config(image = self.imagemBotaoAdd, height=26, width=36)
        bVertice.grid(row=1, column=2, padx=15, pady=10, stick="W")

    def addVertice(self, eNome, varNome):
        global NOME_VERTICE
        NOME_VERTICE = NOME_VERTICE + 1
        varNome.set("V%s" % NOME_VERTICE)
        eNome.delete(0, END)
        eNome.insert(0, "V%s" % NOME_VERTICE)
        
        self.grafo.criarVertice(varNome.get())
        self.atualizaTela()


    def atualizaTela(self):
        self.grafo.carregarImagem()
        self.atualizaCanvas()
        self.incrementaAtualizacao()

    def criaTela(self):  
        self.root.title("GrafoApp")
        width_tela = self.root.winfo_screenwidth()
        height_tela = self.root.winfo_screenheight()
        self.root.geometry("{}x{}+{}+{}".format(width_tela, height_tela, 0, 0))   #resolução 800x600 - 1024x768 - 1280x720  - 1280x800 - 1280x698 - 1366x768
        self.center(self.root)
        self.root.bind('<Escape>',lambda e: self.root.destroy())

    def chamaTela(self):
        self.root.mainloop()

    def criaCanvas(self):       
        self.image = PIL.Image.open(Config.DIRETORIO_PADRAO_IMAGEM)
        imagemAjustada = ImagemUtil.ajustaImagem(self.image)
        self.imageTkinter = ImageTk.PhotoImage(imagemAjustada)
        self.update_img_canvas = self.canvas.create_image(ImagemUtil.WIDTH, ImagemUtil.HEIGHT, anchor = NW, image=self.imageTkinter)
        TelaUtil.createScrollbar('both', self.canvas, self.frameImagem)
        self.canvas.grid(row=0, column=0, rowspan=300, sticky='NW', ipady=0)

    def atualizaCanvas(self):
        self.image = PIL.Image.open(Config.DIRETORIO_PADRAO_IMAGEM)
        imagemAjustada = ImagemUtil.ajustaImagem(self.image)
        self.imageTkinter = ImageTk.PhotoImage(imagemAjustada)
        self.canvas.itemconfig(self.update_img_canvas , image=self.imageTkinter)

    def criarBotoesMetodosGrafo(self):
        self.btnGerarGrafo = Button(self.frameBotoes, relief="groove", border=3, text="Gerar o Grafo")
        self.btnGerarGrafoBuscaLargura = Button(self.frameBotoes, relief="groove", border=3, text="Método Busca em Largura")
        self.btnGerarGrafoBuscaProfundidade = Button(self.frameBotoes, relief="groove", border=3, text="Método Busca em Profundidade")
        self.btnGerarGrafoPrim = Button(self.frameBotoes, relief="groove", border=3, text="Método PRIM")
        self.btnVerificarGrafoPlanar = Button(self.frameBotoes, relief="groove", border=3, text="Verificar Planaridade", command=self.popupVerificarPlanaridade)
        self.btnGerarGrafo.grid(row=0, column=0, padx=10, pady=2, stick= "W")
        self.btnGerarGrafoBuscaLargura.grid(row=1, column=0, padx=10, pady=2, stick= "W")
        self.btnGerarGrafoBuscaProfundidade.grid(row=2, column=0, padx=10, pady=2, stick= "W")
        self.btnGerarGrafoPrim.grid(row=3, column=0, padx=10, pady=2, stick= "W")
        self.btnVerificarGrafoPlanar.grid(row=4, column=0, padx=10, pady=2, stick= "W")

    def popupVerificarPlanaridade(self):
        qtde_atualizacao = self.getAtualizacao() + 1
        popup = Tk()
        popup.withdraw()

        if qtde_atualizacao > (len(self.grafo.getVertices()) + len(self.grafo.getArestas())):
            if self.grafo.grafoConvexoEhPlanar():
                messagebox.showinfo("Information","O grafo é planar!")
            else:
                messagebox.showinfo("Information","O grafo é não é planar!")
            qtde_atualizacao = 0

tela = TelaPrincipal()
tela.criaTela()
tela.chamaTela()


