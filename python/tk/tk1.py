#!/usr/bin/python3

from tkinter import *

top=Tk()
top.geometry("200x200")
bt1=Button(top,text="Quit",bg="pink",command=top.quit)
bt1.pack(side=LEFT)
top.mainloop()
