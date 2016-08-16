#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe
from tkinter import *
from tkinter import ttk


def switch():
   str = label_string.get()
   if str == "True":
       label_string.set("False")
   else:
       label_string.set("True")


root = Tk()

content = ttk.Frame(root)
content.grid(column=0, row=0, sticky=(E,S,W,N))
root.columnconfigure(0, weight=2)
content.columnconfigure(0, weight=2)


label_string = StringVar()

label = ttk.Label(content, text="True", textvariable=label_string, anchor="center")
label.grid(column=0, row=0, sticky=(W,E))

button = ttk.Button(content, text="switch", command=switch, default="active")
button.grid(column=0, row=1, sticky=(W,E))

button.invoke()


root.mainloop()
