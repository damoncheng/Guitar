from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Key:

    frame = ""
    key_combobox = ""
    key_combobox_var = ""
    key_desc_label = ""
    key_tuple = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    key_label = [0 for i in range(7)]
    key_label_var = ["" for i in range(7)]

    def __init__(self,root):
        self.create(root)

    def create(self, root):
        self.frame = Frame(root)
        #self.frame.rowconfigure(0, weight=1)
        #self.frame.columnconfigure(0, weight=1)
        
        for i in range(7):
            self.frame.columnconfigure(i, weight=1)

        self.key_desc_label = ttk.Label(self.frame, text="Key:")
        self.key_desc_label.grid(column=0, row=0, padx=(0,2), sticky="e")
        self.key_combobox = ttk.Combobox(self.frame, textvariable=self.key_combobox_var, width=2)
        self.key_combobox["value"] = self.key_tuple
        self.key_combobox.current(0)
        self.key_combobox.grid(column=1, row=0, pady=20, padx=(2,0), sticky="w")

        for i in range(7):
            self.key_label[i] = ttk.Label(self.frame, textvariable=self.key_label_var[i], text=self.key_tuple[i], pad=15, relief="solid", borderwidth=5)
            self.key_label[i].grid(column=i, row=1, sticky="sn")

    def hide(self):
        self.frame.grid_remove()
        
    def show(self, current, root):
        current.hide()
        self.frame.grid(column=0, row=0, sticky="eswn")
        return self
