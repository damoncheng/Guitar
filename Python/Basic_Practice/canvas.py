#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0
color = "black"


def xy(event):
    global lastx, lasty
    #lastx, lasty = event.x, event.y
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def addLine(event):
    global lastx, lasty
    #canvas.create_line(lastx, lasty, event.x, event.y, fill=color, width=5, tags="currentline")
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags="currentline")
    lastx, lasty = x, y

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 2000, 2000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=1, row=1,sticky=(S,E))

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
canvas.bind("<ButtonPress-1>", xy)
canvas.bind("<Button1-Motion>", addLine)

'''
def setColor(newcolor):
    global color
    color = newcolor


id = canvas.create_rectangle((10,10,30,30), fill="red")
canvas.tag_bind(id, "<Button-1>", lambda x:setColor("red"))
id = canvas.create_rectangle((10,35,30,55), fill="blue")
canvas.tag_bind(id, "<Button-1>", lambda x:setColor("blue"))
id = canvas.create_rectangle((10,60,30,80), fill="black")
canvas.tag_bind(id, "<Button-1>", lambda x:setColor("black"))
'''

def doneStroke(event):
    canvas.itemconfigure("currentline", width=1)

canvas.bind("<B1-ButtonRelease>", doneStroke)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag("all", "paletteSelected")
    canvas.itemconfigure("palette", outline="white")
    canvas.addtag("paletteSelected", "withtag", "palette%s" % color)
    canvas.itemconfigure("paletteSelected", outline="#999999")

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x:setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x:setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x:setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)


root.mainloop()
