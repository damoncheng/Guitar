#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk

root = Tk()

l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))

s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
#ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))

t = Text(root, width=40, height=10)
t.grid(column=2, row=0)
t.insert("end", "123")
t.insert("1.1", "456")

#pi = DoubleVar()
p = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode="determinate")
p.grid(column=3, row=0)
p.start()
#pi.set(10.0)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

for i in range(1,101):
    l.insert("end", "Line %d of 100" % i)

#s.set(0.5,0)
l.see(50)

root.mainloop()
