#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()

appHighlightFont = font.Font(family="time", size=12, weight="bold")
l = ttk.Label(root, text="Label", font=appHighlightFont, foreground="#3FF")
l.grid(column=0, row=0)

imgobj = PhotoImage(file='img/desktop.png')
b = ttk.Button(root, compound="none", image=imgobj)

b.grid(column=0, row=1)

root.mainloop()
