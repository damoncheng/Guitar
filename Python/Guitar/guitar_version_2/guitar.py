#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk

from welcome import *
from key import *

def show(replace, root):
   global current 
   current = replace.show(current, root)


root = Tk()
root.option_add('*tearOff', FALSE)
root.title('The World Of Guitar')
root.geometry("1000x700+150+50")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

menubar = Menu(root)
root['menu'] = menubar

menu_basis = Menu(menubar, name="basis")
menubar.add_cascade(menu=menu_basis, label="Basis")

key = Key(root)
welcome = Welcome(root)
current = welcome

menu_basis.add_command(label="Key", command=lambda: show(key, root))
show(welcome, root)

root.mainloop()
