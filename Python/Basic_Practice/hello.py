#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk
root = Tk()
content = ttk.Frame(root, relief="solid", borderwidth=10, width=20, height=20)
ttk.Checkbutton(root, text="two").grid(column=1, row=0)
content.grid(column=0,row=0,sticky="wsne",ipadx=20)
b = ttk.Button(content, text="Hello One")
b.grid(column=0, row=0, sticky="se", ipadx=20)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)

root.mainloop()
