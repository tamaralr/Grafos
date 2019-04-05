from tkinter import *

class Tela(object):

    def __init__(self,requestMessage):
        self.root = Tk()
        self.root.attributes('-alpha', 1.0)
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(requestMessage)

    def acceptInput(self,requestMessage):
        r = self.frame

        k = Label(r,text=requestMessage)
        k.pack(side='left')
        self.e = Entry(r,text='Name')
        self.e.pack(side='left')
        self.e.focus_set()
        b = Button(r,text='okay',command=self.gettext)
        b.pack(side='right')

    def gettext(self):
        self.string = self.e.get()
        self.root.destroy()

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()


    @classmethod
    def show_dialog(Tela, requestMessage):
        msgBox = Tela(requestMessage)
        msgBox.waitForInput()
        return msgBox.getString()

    @classmethod
    def print(Tela, Message):
        root = Tk()
        T = Text(root, height=2, width=30)
        T.pack()
        T.insert(END, Message)
        mainloop()

    @classmethod
    def input_grafo(Tela, titulo, aresta, vertice):
        root = Tk()
        frame = Frame(root)
        l1 = Label(frame,text=titulo)
        l1.pack(side='left')
        g1 = Entry(frame,text=titulo)
        g1.pack(side='left')

        frame2 = Frame(root)
        l2 = Label(frame2,text=aresta)
        l2.pack(side='left')
        g2 = Entry(frame2,text=aresta)
        g2.pack(side='left')
        
        frame3 = Frame(root)
        l3 = Label(frame3,text=vertice)
        l3.pack(side='left')
        g3 = Entry(frame3,text=vertice)
        g3.pack(side='left')
        
        root.mainloop()



# var = takeInput.getText('enter your name')
#print("Var:", var)