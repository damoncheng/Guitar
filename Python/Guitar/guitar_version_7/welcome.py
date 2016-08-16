from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
class Welcome:

    frame = ""
    label = ""
    image = ""

    def __init__(self, root):
        self.create(root)

    def create(self, root):
        self.frame = Frame(root)
        self.frame.grid(column=0,row=0,sticky="eswn")
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        welcome_font = font.Font(family='Helvetica', size=12, weight="bold")
        self.image= PhotoImage(file="./img/welcome.gif")
        self.label = ttk.Label(self.frame, image=self.image, anchor="center")
        self.label.grid(column=0, row=0, sticky="eswn")

    def hide(self):
        self.frame.grid_remove()

    def show(self, current, root):
        current.hide()
        self.frame.grid(column=0, row=0, sticky="eswn")
        return self
