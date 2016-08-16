from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

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
    key_chord_progression = [ 0 for i in range(8) ]
    key_chord_progression_tuple = ("I(135)", "II(246)", "III(357)", "IV(461)", "V(572)", "VI(613)", "VII(5724)")

    key_chord_tuple = (
                        ("C key:", "key_chord_C", "key_chord_C_tuple", "key_chord_C_fingering_tuple"), 
                        ("D key:", "key_chord_D", "key_chord_D_tuple", "key_chord_D_fingering_tuple"), 
                        ("E key:", "key_chord_E", "key_chord_E_tuple", "key_chord_E_fingering_tuple"), 
                        ("F Key:", "key_chord_F", "key_chord_F_tuple", "key_chord_F_fingering_tuple"), 
                        ("G key:", "key_chord_G", "key_chord_G_tuple", "key_chord_G_fingering_tuple"), 
                        ("A key:", "key_chord_A", "key_chord_A_tuple", "key_chord_A_fingering_tuple"), 
                        ("B key:", "key_chord_B", "key_chord_B_tuple", "key_chord_B_fingering_tuple")
                    )

    key_chord_C = [ 0 for i in range(8) ]
    key_chord_C_tuple = ("C", "Dm", "Em", "F", "G", "Am", "G7")
    key_chord_C_fingering_tuple = (
                [("1", 1, 5), ("2", 2, 3), ("x", 0, 1), ("3", 3, 2)] , 
                [("x", 0, 1), ("1", 1, 6), ("2", 2, 4), ("4", 3, 5)],
                [("2", 2, 2), ("3", 2, 3)],
                [("all", "", 1), ("2", 2, 4), ("3", 3, 2), ("4", 3, 3)],
                [("1", 2, 2), ("2", 3, 1), ("3", 3, 6)],
                [("1", 1, 5), ("2", 2, 3), ("3", 2, 4)],
                [("1", 1, 6), ("2", 2, 2), ("3", 3, 1)]
            )
    key_chord_D = [ 0 for i in range(8) ]
    key_chord_D_tuple = ("D", "Em", "F#m", "G", "A", "Bm", "A7")
    key_chord_D_fingering_tuple = (
                [("x", 0, 1), ("1", 2, 4), ("2", 2, 6), ("3", 3, 5)],
                [("2", 2, 2), ("3", 2, 3)],
                [("all", "2", 1), ("3", 3, 2), ("4", 3, 3)],
                [("1", 2, 2), ("2", 3, 1), ("3", 3, 6)],
                [("1", 2, 3), ("2", 2, 4), ("3", 2, 5)],
                [("all", "2", 1), ("2", 2, 5), ("3", 3, 3), ("4", 3, 4)],
                [("part", 3, 2), ("2", 3, 6), ("x", 0, 1)]
            )
    key_chord_E = [ 0 for i in range(8) ]
    key_chord_E_tuple = ("E", "F#m", "G#m", "A", "B", "C#m", "B7")
    key_chord_E_fingering_tuple = (
                [("1", 1, 4), ("2", 2, 2), ("3", 2, 3)],
                key_chord_D_fingering_tuple[2],
                [("all", "4", 1), ("3", 3, 2), ("4", 3, 3)],
                key_chord_D_fingering_tuple[4],
                [("all", "2", 1), ("2", 3, 3), ("3", 3, 4), ("4", 3, 5)],
                [("1", 1, 4), ("2", 2, 3), ("3", 2, 5)],
                [("x", 0, 1), ("1", 1, 3), ("2", 2, 2), ("3", 2, 4), ("4", 2, 6)]
            )
    key_chord_F = [ 0 for i in range(8) ]
    key_chord_F_tuple = ("F", "Gm", "Am", "Bb", "C", "Dm", "C7")
    key_chord_F_fingering_tuple = (
                key_chord_C_fingering_tuple[3],
                [("all", "3", 1), ("2", 2, 4), ("3", 3, 2), ("4", 3, 3)],
                key_chord_C_fingering_tuple[5],
                [("all", "", 1), ("2", 3, 3), ("3", 3, 4), ("4", 3, 5)],
                key_chord_C_fingering_tuple[0],
                key_chord_C_fingering_tuple[1],
                [("1", 1, 5), ("2", 2, 3), ("3", 3, 2), ("4", 3, 4)]
            )
    key_chord_G = [ 0 for i in range(8) ]
    key_chord_G_tuple = ("G", "Am", "Bm", "C", "D", "Em", "D7")
    key_chord_G_fingering_tuple = (
                key_chord_C_fingering_tuple[4],
                key_chord_C_fingering_tuple[5],
                key_chord_D_fingering_tuple[5],
                key_chord_C_fingering_tuple[0],
                key_chord_D_fingering_tuple[0],
                key_chord_C_fingering_tuple[2],
                [("1", 1, 5), ("2", 2, 4), ("3", 2, 6)]
            )
    key_chord_A = [ 0 for i in range(8) ]
    key_chord_A_tuple = ("A", "Bm", "C#m", "D", "E", "F#m", "E7")
    key_chord_A_fingering_tuple = (
                key_chord_D_fingering_tuple[4],
                key_chord_D_fingering_tuple[5],
                [("all", "4", 1), ("2", 2, 5), ("3", 3, 3), ("4", 3, 4)],
                key_chord_D_fingering_tuple[0],
                key_chord_E_fingering_tuple[0],
                key_chord_D_fingering_tuple[2],
                [("1", 1, 4), ("2", 2, 2), ("3", 2, 3), ("4", 3, 5)]
            )
    key_chord_B = [ 0 for i in range(8) ]
    key_chord_B_tuple = ("B", "C#m", "D#m", "E", "F#", "G#m", "F#7")
    key_chord_B_fingering_tuple = (
                key_chord_E_fingering_tuple[4],
                key_chord_A_fingering_tuple[2],
                [("all", "6", 1), ("2", 2, 5), ("3", 3, 3), ("4", 3, 4)],
                key_chord_E_fingering_tuple[0],
                [("all", "2", 1), ("2", 2, 4), ("3", 3, 2), ("4", 3, 3)],
                [("all", "4", 1), ("3", 3, 2), ("4", 3, 3)],
                [("all", "2", 1), ("3", 3, 2), ("2", 2, 4)]
            )

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

        #frame which own Combobox
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

        #roll call and musical alphabet label
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

        #chord area
        self.key_chord_desc_label = ttk.Label(self.frame, text="Chord:")
        self.key_chord_desc_label.grid(column=0, row=3, pady=20, padx=(5,0), sticky="w")

        self.key_chord_progression[0] = ttk.Label(self.frame, text="Progression:")
        self.key_chord_progression[0].grid(column=0, row=4, sticky="e")
        for i in range(7):
            self.key_chord_progression[i+1] = ttk.Label(self.frame, text=self.key_chord_progression_tuple[i], width=10, anchor="center")
            self.key_chord_progression[i+1].grid(column=(i+1), row=4)

        key_desc_tuple = (110, 40)
        chord_desc_tuple = (55, 20)
        chord_start_x = 30
        chord_start_y = 30
        first_fret_sixth_string_tuple = (30, 35)
        chord_x_step = 10
        chord_y_step = 10
        chord_font = font.Font(family="time", size=7, slant="italic", weight="bold")

        for key in range(7):

            key_text = self.key_chord_tuple[key][0]
            key_chord_current = eval("self." + self.key_chord_tuple[key][1])
            key_chord_current_tuple = eval("self." + self.key_chord_tuple[key][2])
            key_chord_current_fingering_tuple = eval("self." + self.key_chord_tuple[key][3])

            for i in range(8):
                key_chord_current[i] = Canvas(self.frame,  height=60)
                key_chord_current[i].grid(column=(i), row=5 + key, sticky="eswn")
                if i == 0:
                    key_chord_current[i].create_text(key_desc_tuple, text=key_text, anchor="e")
                    continue

                key_chord_current[i].create_text(chord_desc_tuple, text=key_chord_current_tuple[i-1])

                key_chord_current[i].create_line(chord_start_x, chord_start_y                   , chord_start_x + 5 * chord_x_step, chord_start_y)
                key_chord_current[i].create_line(chord_start_x, chord_start_y +     chord_y_step, chord_start_x + 5 * chord_x_step, chord_start_y + chord_y_step)
                key_chord_current[i].create_line(chord_start_x, chord_start_y + 2 * chord_y_step, chord_start_x + 5 * chord_x_step, chord_start_y + 2 * chord_y_step)
                key_chord_current[i].create_line(chord_start_x, chord_start_y + 3 * chord_y_step, chord_start_x + 5 * chord_x_step, chord_start_y + 3 * chord_y_step)

                key_chord_current[i].create_line(chord_start_x,                    chord_start_y, chord_start_x,                    chord_start_y + 3 * chord_y_step)
                key_chord_current[i].create_line(chord_start_x +     chord_x_step, chord_start_y, chord_start_x + chord_x_step,     chord_start_y + 3 * chord_y_step)
                key_chord_current[i].create_line(chord_start_x + 2 * chord_x_step, chord_start_y, chord_start_x + 2 * chord_x_step, chord_start_y + 3 * chord_y_step)
                key_chord_current[i].create_line(chord_start_x + 3 * chord_x_step, chord_start_y, chord_start_x + 3 * chord_x_step, chord_start_y + 3 * chord_y_step)
                key_chord_current[i].create_line(chord_start_x + 4 * chord_x_step, chord_start_y, chord_start_x + 4 * chord_x_step, chord_start_y + 3 * chord_y_step)
                key_chord_current[i].create_line(chord_start_x + 5 * chord_x_step, chord_start_y, chord_start_x + 5 * chord_x_step, chord_start_y + 3 * chord_y_step)

                one_list =  key_chord_current_fingering_tuple[i - 1]
                for one_point in one_list: 
                    if one_point[0] == "all":
                        if one_point[1] != "":
                            key_chord_current[i].create_text(
                                (
                                    first_fret_sixth_string_tuple[0] - chord_x_step,
                                    first_fret_sixth_string_tuple[1] + (one_point[2] - 1) * chord_y_step
                                ),
                                text = one_point[1],
                                font = chord_font
                            )

                        key_chord_current[i].create_line(
                                first_fret_sixth_string_tuple[0] - 0.5 * chord_x_step,
                                first_fret_sixth_string_tuple[1] + (one_point[2] - 1) * chord_y_step,
                                first_fret_sixth_string_tuple[0] + (5 + 1) * chord_x_step,
                                first_fret_sixth_string_tuple[1] + (one_point[2] - 1) * chord_y_step,
                                arrow="last"
                        )

                        key_chord_current[i].create_text(
                            (
                                first_fret_sixth_string_tuple[0] + (5 + 1.5) * chord_x_step,        
                                first_fret_sixth_string_tuple[1] + (one_point[2] - 1) * chord_y_step
                            ),
                            text="1",
                            font = chord_font
                        )
                    elif one_point[0] == "part":
                        key_chord_current[i].create_line(
                                first_fret_sixth_string_tuple[0] + (one_point[1] - 1) * chord_x_step - 0.5 * chord_x_step,
                                first_fret_sixth_string_tuple[1] + (one_point[2] - 1) * chord_y_step,
                                first_fret_sixth_string_tuple[0] + (5 + 1) * chord_x_step,
                                first_fret_sixth_string_tuple[1] + (one_point[2] - 1) * chord_y_step,
                                arrow="last"
                        )
                        key_chord_current[i].create_text(
                            (
                                first_fret_sixth_string_tuple[0] + (5 + 1.5) * chord_x_step,        
                                first_fret_sixth_string_tuple[1] + (one_point[2] - 1) * chord_y_step
                            ),
                            text="1",
                            font = chord_font
                        )

                    else:
                        key_chord_current[i].create_text(
                            (
                                first_fret_sixth_string_tuple[0] + (one_point[2] - 1)*chord_x_step, 
                                first_fret_sixth_string_tuple[1] + (one_point[1] - 1)*chord_y_step
                            ),
                            text=one_point[0], 
                            font = chord_font
                        )

    def hide(self):
        self.frame.grid_remove()
        
    def show(self, current, root):
        current.hide()
        self.frame.grid(column=0, row=0, sticky="eswn")
        return self
