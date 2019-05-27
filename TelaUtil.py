from tkinter import *

WIDTH = 700
HEIGHT = 600
ROWSPAN = 300

class TelaUtil:

    @classmethod
    def createScrollbar(self, typeOrientation, component, frame):
        
        if typeOrientation == 'horizontal':
            s = Scrollbar(frame, orient=typeOrientation)
            s['command'] =component.xview
            component['xscrollcommand'] = s.set
            s.grid(row=0, column=0, rowspan=ROWSPAN, sticky='NESW')
        elif typeOrientation == 'vertical':
            s = Scrollbar(frame, orient=typeOrientation)
            s['command'] = component.yview
            component['yscrollcommand'] = s.set
            s.grid(row=1, column=1, rowspan=ROWSPAN, sticky='NSW')
        elif typeOrientation == 'both':
            v = Scrollbar(frame, orient=VERTICAL)
            v['command'] = component.yview
            component['yscrollcommand'] = v.set

            h = Scrollbar(frame, orient=HORIZONTAL)
            h['command'] = component.xview
            component['xscrollcommand'] = h.set
            component.config(width=WIDTH, height=HEIGHT)

            v.grid(row=1, column=1, rowspan=ROWSPAN,sticky='NSW')
            h.grid(row=ROWSPAN, column=0, sticky='NESW')
        else:
            print('ERRO! Não existe essa opção.')
