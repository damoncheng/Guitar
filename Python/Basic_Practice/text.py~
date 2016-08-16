#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

label_string = StringVar()
label = ttk.Label(root, text="", textvariable=label_string)
label.grid(column=0, row=1)

text = Text(root, width=40, height=10, undo=True)
text.grid(column=0, row=0, sticky="ESWN")

text.insert('1.0', "1 here is my text to insert\n")
text.insert('1.end + 1 chars', '2 here is my text to insert\n')
text.insert('2.end + 1 chars', '3 here is my text to insert\n')

def select_text(event):
    if text.tag_ranges("sel"):
        (text_start, text_end) = text.tag_ranges("sel")
        label_string.set(text.get(text_start, text_end)) 
    else:
        label_string.set("") 


def un_do(event):
    label_string.set("hello")
    text.edit_undo()

def re_do(event):
    text.edit_redo()
        

text.bind("<<Selection>>", select_text)
text.bind("<Control-z>", un_do)
text.bind("<Control-y>", re_do)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


root.mainloop()
