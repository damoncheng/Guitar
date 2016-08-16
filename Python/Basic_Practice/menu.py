#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk


def newFile():
    ls.set("new")

def openFile():
    ls.set("open")

root = Tk()
root.option_add('*tearOff', FALSE)

menubar = Menu(root)
root['menu'] = menubar

menu_file = Menu(menubar, name="file")
menubar.add_cascade(menu=menu_file,label="File")

menu_file.add_command(label='New', command=newFile)
menu_file.add_command(label='Open', command=openFile, accelerator="Control+O")
menu_file.add_command(label='Close', command=newFile)
menu_file.add_separator()

check = StringVar()
menu_file.add_checkbutton(label="Check", variable=check, onvalue=1, offvalue=0)
radio = StringVar()
menu_file.add_radiobutton(label="One", variable=radio, value=1)
menu_file.add_radiobutton(label="Two", variable=radio, value=2)

ls = StringVar()
l = ttk.Label(root, text="1", textvariable=ls)
ls.set("start")
l.grid(column=0, row=0)


menu = Menu(root)
for i in ('One', 'Two', 'Three'):
    menu.add_command(label=i)
if (root.tk.call('tk', 'windowingsystem')=='aqua'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))



root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
