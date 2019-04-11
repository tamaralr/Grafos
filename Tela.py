from tkinter import *
from functools import partial

QTDE_VERTICE = 0
FRAMES = []
class TelaPrincipal:

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
        self.photo=PhotoImage(file="add-icon.png")
        # flat, groove, raised, ridge, solid, or sunken
        self.painel = PanedWindow(self.root, relief="ridge", border=2)
        self.painel.grid(column=0, row=0, sticky='W', ipadx=100, ipady=100)


        self.frame = LabelFrame(self.painel, text="Tela Grafo")
        self.frame.grid(column=0,row=1, stick="W", padx=0,pady=5, ipadx=50)
        self.value = any  
        self.label = any
        self.entradaDeDados(self.frame)

        self.cf = LabelFrame(self.painel, text="Dados de Entrada: ")
        self.cf.grid(column=0, row=2, sticky='W', pady=5)

        self.string_vars = []
        self.fruit = ("Vertice 0", "Vertice 1", "Vertice 2", "Vertice 3")
        self.criaEntradaDados()


    def criaEntradaDados(self):
        for f in self.fruit:
            i = len(self.string_vars)
            self.string_vars.append(StringVar())
            self.string_vars[i].trace("w", lambda name, index, mode, var=self.string_vars[i], i=i:self.entryupdate(var, i))
            Label(self.cf, text=f).grid(column=0, row=i)
            entryDados = Entry(self.cf, width=15, textvariable=self.string_vars[i]).grid(column=1, row=i, padx=5)
    
    def entryupdate(self, sv, i):
        print(sv, i, self.fruit[i], sv.get())


    def entradaDeDados(self, frame):
        self.value = IntVar()
        self.label = Label( self.frame, text="R")
        self.label.grid(column=0, row=5)
        txtQtdeVert = Label(frame, text="Cria Vertice: ")
        txtQtdeVert.grid(column=0,row=1, stick="W")
        e = Entry(frame, width=8,textvariable=self.value)
        e.grid(column=6, row=1, padx=22)
        e.bind('<Return>', self.convert)
        e.focus()
        
        b = Button(frame, command=self.convert,relief="groove", border=3)
        b.config(image = self.photo, height=26, width=56)
        b.grid(column=6, row=5, padx=10, pady=10)


    def convert(self, event=None):
        global QTDE_VERTICE 
        try:
            print(self.value.get())
            QTDE_VERTICE = self.value.get()
            self.label.config(text=QTDE_VERTICE)
        except TclError:
            self.label.config(text="Not an integer")


    def criaTela(self):  
        self.root.title("GrafoApp")
        width_tela = self.root.winfo_screenwidth()
        height_tela = self.root.winfo_screenheight()
        self.root.geometry("{}x{}+{}+{}".format(width_tela, height_tela, 0, 0))   #resolução 800x600 - 1024x768 - 1280x720  - 1280x800 - 1280x698 - 1366x768
        self.center(self.root)
        self.root.bind('<Escape>',lambda e: self.root.destroy())

    def chamaTela(self):
        self.root.mainloop()

    def mudaFrame(self):
        pass


# tela = TelaPrincipal()
# tela.criaTela()
# tela.chamaTela()
