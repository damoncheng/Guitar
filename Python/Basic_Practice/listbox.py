#!C:\Users\damoncheng\AppData\Local\Programs\Python\Python35\python.exe

from tkinter import *
from tkinter import ttk

root = Tk()

countrycodes=('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'jp',
        'mx', 'nl', 'no', 'es', 'se', 'ch')

countrynames=('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', \
        'Norway', 'Spain', 'Sweden', 'Switzerland')

cnames = StringVar(value=countrynames)
populations = {'ar':41000000, 'au':21179211, 'be':10584534, 'br':185971537, \
'ca':33148682, 'cn':1323128240, 'dk':5457415, 'fi':5302000, 'fr':64102140, 'gr':11147000, \
'in':1131043000, 'it':59206382, 'jp':127718000, 'mx':106535000, 'nl':16402414, \
'no':4738085, 'es':45116894, 'se':9174082, 'ch':7508700}

# Names of the gifts we can send
gifts = { 'card':'Greeting card', 'flowers':'Flowers', 'nastygram':'Nastygram'}
# State variables
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of %s (%s) is %d" % (name, code, popn))
    sentmsg.set("")

def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        # Gift sending left as an exercise to the reader
        sentmsg.set("Sent %s to leader of %s" % (gifts[gift.get()], name))

c = ttk.Frame(root, padding=(5,5,12,0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lbox = Listbox(c, listvariable=cnames, height=5)
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbox.selection_set(0)
lbox.bind("<<ListboxSelect>>", showPopulation)
lbox.bind("<Double-1>", sendGift)
root.bind("<Return>", sendGift)
for i in range(0, len(countrynames), 2):
    lbox.itemconfigure(i, background="#f0f0ff")


lbl = ttk.Label(c, text="Send to country's leader")
lbl.grid(column=1, row=0, padx=10, pady=5)


g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value="card")
g2 = ttk.Radiobutton(c, text=gifts["flowers"], variable=gift, value="flowers")
g3 = ttk.Radiobutton(c, text=gifts["nastygram"], variable=gift, value="nastygram")
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)
g3.grid(column=1, row=3, sticky=W, padx=20)
gift.set('card')

send = ttk.Button(c, text="Send Gift", command=sendGift, default='active')
send.grid(column=2, row=4, sticky=E)

sentlbl = ttk.Label(c, textvariable=sentmsg, anchor="center")
sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
sentmsg.set("")

status = ttk.Label(c, textvariable=statusmsg, anchor=W)
status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
showPopulation()


c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)
root.mainloop()
