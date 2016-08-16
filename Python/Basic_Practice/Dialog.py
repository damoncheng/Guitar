#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox

root = Tk()

#filename = filedialog.askopenfilename()
#filename = filedialog.asksaveasfilename()
#dirname = filedialog.askdirectory()

#colorchooser.askcolor(initialcolor='#ff0000')

#messagebox.showinfo(message="Have a good day")

#s = ttk.Separator(root, orient=HORIZONTAL)

'''
b1 = ttk.Button(root, text="Hello One")
b1.grid(column=1, row=0)
b2 = ttk.Button(root, text="Hello two")
b2.grid(column=1, row=2, sticky="ESWN")
s = ttk.Separator(root, orient=HORIZONTAL)
s.grid(column=1,row=1, sticky="ESWN")
root.rowconfigure(2, weight=1)
root.columnconfigure(1, weight=1)
'''

'''
lf = ttk.Labelframe(root, text="label frame")
lf.grid(column=1, row=0)

b1 = ttk.Button(lf, text="Hello One")
b1.grid(column=0, row=0)


p = ttk.Panedwindow(root, orient=VERTICAL)
f1 = ttk.Labelframe(p, text="Pane1", width=100, height=100)
f2 = ttk.Labelframe(p, text="Pane2", width=100, height=100)

p.add(f1)
p.add(f2)
p.grid(column=0, row=0)
'''

n = ttk.Notebook(root)
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
n.add(f1, text='One')
n.add(f2, text='Two')

n.grid(column=0, row=0)

n.tab(f1, text="sn")

root.mainloop()

