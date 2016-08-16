#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk


def tree_event(event):
    label_string.set(tree.selection())   


root = Tk()

label_string = StringVar()
label = ttk.Label(root, text="label", textvariable=label_string)
label_string.set("label")
label.grid(column=0, row=0)

tree = ttk.Treeview(root)
tree['columns'] = ('size', 'text')
tree.column('size', anchor='center')
tree.column('text', anchor='center')
tree.heading("size", text="Size")
tree.heading("text", text="Text")

tree.insert('', 'end', 'widgets', text='Widget Tour', values=(1, "123"))
tree.insert('', 0, 'gallery', text='Applications')
id = tree.insert('', 'end', text="Tutorial")
tree.insert('widgets', 'end', text='Canvas')

tree.bind('<<TreeviewSelect>>', tree_event)


tree.grid(column=0, row=1)
root.mainloop()
