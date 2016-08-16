#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe
from tkinter import *
from tkinter import ttk

#------------point---------------#
'''
a = [1,2,3]
#b = a
b = a[:]
b[0] = 5

print a
'''




#----------calculate------------#
'''
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048*value*10000.0+0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
#mainframe.columnconfigure(0, weight=1)
#mainframe.rowconfigure(0,weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2,row=1,sticky=(W,E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2,row=2,sticky=(W,E))
ttk.Button(mainframe,text="Calculate",command=calculate).grid(column=3,row=3,sticky=W)

ttk.Label(mainframe,text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe,text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe,text="meters").grid(column=3,row=2,sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)


feet_entry.focus()

root.mainloop()
'''

#-----------practice from book--------------#
'''
root = Tk()

content = ttk.Frame(root)
content.grid(column=0,row=0,sticky=(N,W,E,S))
path_content = str(content)
ttk.Button(content, text=path_content).grid(column=0,row=0,sticky=(N,W,E,S))

root.mainloop()
'''

'''
root = Tk()

button = ttk.Button(root, text="Hello", command="buttonpressed")
button["text"] = "hello one"
button.configure(text="hello two")
button.grid()

root.mainloop()
'''

'''
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()
'''

#---------------basic widgets--------------------#
'''
root = Tk()
content = ttk.Frame(root)
content.grid(column=0,row=0,sticky=(N,W,E,S))
#root.columnconfigure(0,weight=2)
#content.columnconfigure(0,weight=2)
#content["width"] = 200
#content["height"] = 200
content["borderwidth"] = 5
content["relief"] = "solid"
content["padding"] = (5,10)
ttk.Button(content, text="click one").grid(column=0,row=0,sticky=(N,W,E,S))
ttk.Button(content, text="click two").grid(column=1,row=0,sticky=(N,W,E,S))
label = ttk.Label(content, text="click three", anchor="center", relief="solid", foreground="red", background="yellow")
label["font"] = "TkIconFont"
label.grid(column=0,row=1,sticky=(N,W,E,S))

root.mainloop()
'''

root = Tk()  
sl = Scrollbar(root)  
sl.set(0.5,0)  
sl.pack()  
root.mainloop()  




