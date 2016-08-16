#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe
from tkinter import *
from tkinter import ttk

def entry_validate():
    label_string.set("entry_validate")

def metricChanged():
    #value = measureSystem.get()
    #label_string.set(value)
    pass

root = Tk()
root.columnconfigure(0, weight=2)
root["pady"] = 10

label_string = StringVar()
check_string = StringVar()
radio_string = StringVar()
entry_string = StringVar()
combobox_string = StringVar()
measureSystem = StringVar()
check_string.set("Use Metric")

label = ttk.Label(root, text="", textvariable=label_string, anchor="center")
check = ttk.Checkbutton(root, text='Use Metric', textvariable=check_string,
        command=metricChanged, variable=measureSystem,
        onvalue='metric', offvalue='imperial')

home = ttk.Radiobutton(root, text="Home", command=metricChanged, 
        variable=radio_string, value='home')
office = ttk.Radiobutton(root, text="Office", command=metricChanged,
        variable=radio_string, value="office")
cell = ttk.Radiobutton(root, text="Mobile", command=metricChanged,
        variable=radio_string, value="cell")
name = ttk.Entry(root, textvariable=entry_string, #show="*",# 
        validate="focusout", validatecommand=entry_validate)

combobox = ttk.Combobox(root, textvariable=combobox_string)
combobox["value"] = ('USA', 'Canada', 'Australia')


name.state(['readonly'])
combobox.state(['readonly'])
entry_string.set("you cann't edit me")
combobox.current(1)

label.grid(column=1, row=0)
check.grid(column=1, row=1)
home.grid(column=0, row=2)
office.grid(column=1, row=2)
cell.grid(column=2, row=2)
name.grid(column=1, row=3)
combobox.grid(column=1, row=4)

#check.invoke()
#flag = home.instate(['alternate'])
#label_string.set(flag)

root.mainloop()
