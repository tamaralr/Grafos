
#no cmd digitar: pip install graphviz
#Adicionar essas PATHs no ambiente de variaveis do win
#baixar o graphviz.msi
#C:/Program Files (x86)/Graphviz2.38/bin/
#C:/Program Files (x86)/Graphviz2.38/bin/dot.exe
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin\\'

from graphviz import Graph

# from tkinter import * 
# root = Tk()
# canvas = Canvas(root, width=500, height=500)
# canvas.pack()
# img = PhotoImage(file='path/your_image.png')
# canvas.create_image(250, 250, image=img)
# root.mainloop()


from graphviz import *
import graphviz as gv
import pylab
import tempfile

dot = gv.Graph()

# print(dot)

dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

# print(dot.source)
texto = """ %s """ % (dot.source)
with open("E:/Users/tlr/OneDrive - UNIVALI/Cursos/Ciencia da Computacao/7 semestre/Grafos/rep/Grafos/arquivo.dot", "a") as arq:
# arq = open('E:/Users/tlr/OneDrive - UNIVALI/Cursos/Ciencia da Computacao/7 semestre/Grafos/rep/Grafos/arquivo.dot', 'w')
	arq.write(texto)
arq.close()


#s.view(tempfile.mktemp('.gv.png'))
# dot.render('dot', 'png', 'test-output/holy-grenade.gv')

#fdp -Tpng -o grafo.png grafo.gv