#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk

root = Tk()

svalue = DoubleVar()
s = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=svalue)
s.grid(column=0, row=0)
svalue.set(50)

root.mainloop()
