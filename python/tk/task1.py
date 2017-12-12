#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

interface = Tk()

def openfile():
    return filedialog.askopenfilename()

button = ttk.Button(interface, text="Open", command=openfile)  # <------
button.grid(column=1, row=1)

interface.mainloop()
