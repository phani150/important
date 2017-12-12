#!/usr/bin/python3
from tkinter import Frame, Tk, BOTH, Text, Menu, END 
from tkinter import filedialog
from tkinter import *

#scrollbar = Scrollbar(root)
#scrollbar.pack(side = RIGHT, fill = Y)
#root.configure(background = "purple")
class Example(Frame):
 
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.initUI()
        items = {"Project1": ["project1","project2","project3"],
                 "Project2": ["project4","project5","project6"]}

        self.the_value = StringVar()
        self.the_value.set("Project")

        self.menubutton = Menubutton(self, bg="Cyan",textvariable=self.the_value, indicatoron=True)
        self.topMenu = Menu(self.menubutton, tearoff=False)
        self.menubutton.configure(menu=self.topMenu)

        for key in sorted(items.keys()):
            menu = Menu(self.topMenu)
            self.topMenu.add_cascade(label=key, menu=menu)
            for value in items[key]:
                menu.add_radiobutton(label=value, variable = self.the_value, value=value)

        self.menubutton.pack()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH)
        menubar = Menu(self.parent,bg='pink')
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar,tearoff=0)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(side= LEFT)

    def onOpen(self):

        ftypes = [('Python files', '*.*'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text
def main():

    root = Tk()
    ex = Example(root)
    root.geometry("5000x5000")
    root.mainloop()

if __name__ == "__main__":
    main()
