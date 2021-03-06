from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Key:

    frame = ""
    key_frame = ""
    key_combobox = ""
    key_combobox_var = ""
    key_desc_label = ""

    roll_call_desc_label = ""
    roll_call_tuple = ("1", "2", "3", "4", "5", "6", "7")
    musical_alphabet_desc_label = ""
    key_tuple_C = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    key_tuple_D = ('D', 'E', 'F#', 'G', 'A', 'B', 'C#')
    key_tuple_E = ('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#')
    key_tuple_F = ('F', 'G', 'A', 'Bb', 'C', 'D', 'E')
    key_tuple_G = ('G', 'A', 'B', 'C', 'D', 'E', 'F#')
    key_tuple_A = ('A', 'B', 'C#', 'D', 'E', 'F#', 'G#')
    key_tuple_B = ('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#')

    roll_call_label = [0 for i in range(7)]
    key_label = [0 for i in range(7)]
    key_label_var = ["" for i in range(7)]

    key_chord_desc_label = ""
    key_chord_C = []
    key_chord_D = []
    key_chord_E = []
    key_chord_F = []
    key_chord_G = []
    key_chord_A = []
    key_chord_B = []

    def __init__(self,root):
        self.create(root)

    def combobox_select(self, event):
        index = self.key_combobox.current()
        select_key = self.key_combobox.get()
        select_key_tuple = eval("self." + "key_tuple_" + select_key)
        for i in range(7):
            self.key_label[i]["text"] = select_key_tuple[i]


    def create(self, root):
        self.frame = Frame(root)
        
        for i in range(8):
            self.frame.columnconfigure(i, weight=1)

        self.key_frame = Frame(self.frame)
        self.key_frame.grid(column=0, row=0, pady=20, padx=(5,0), sticky="w")

        self.key_desc_label = ttk.Label(self.key_frame, text="Key:")
        self.key_desc_label.grid(column=0, row=0)

        self.key_combobox = ttk.Combobox(self.key_frame, textvariable=self.key_combobox_var, width=2)
        self.key_combobox["value"] = self.key_tuple_C
        self.key_combobox.current(0)
        self.key_combobox.grid(column=1, row=0, padx=(2,0))
        self.key_combobox["state"] = "readonly"
        self.key_combobox.bind("<<ComboboxSelected>>", self.combobox_select)

        self.roll_call_desc_label = ttk.Label(self.frame, text="roll call:")
        self.roll_call_desc_label.grid(column=0, row=1, sticky="e")

        for i in range(7):
            self.roll_call_label[i] = ttk.Label(self.frame, text=self.roll_call_tuple[i], width=10,  relief="solid", borderwidth=5)
            self.roll_call_label[i].grid(column=(i+1), row=1, pady=5, sticky="sn")

        self.musical_alphabet_desc_label = ttk.Label(self.frame, text="musical alphabet:")
        self.musical_alphabet_desc_label.grid(column=0, row=2, sticky="e")

        for i in range(7):
            self.key_label[i] = ttk.Label(self.frame, textvariable=self.key_label_var[i], text=self.key_tuple_C[i], width=10, relief="solid", borderwidth=5)
            self.key_label[i].grid(column=(i+1), row=2, pady=5, sticky="sn")

        self.key_chord_desc_label = ttk.Label(self.frame, text="Chord:")
        self.key_chord_desc_label.grid(column=0, row=3, pady=20, padx=(5,0), sticky="w")


    def hide(self):
        self.frame.grid_remove()
        
    def show(self, current, root):
        current.hide()
        self.frame.grid(column=0, row=0, sticky="eswn")
        return self
