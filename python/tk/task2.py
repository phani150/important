#!/usr/bin/python3
from tkinter import Frame, Tk, BOTH, Text, Menu, END 
from tkinter import filedialog

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        

        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.parent,bg='pink')
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar,tearoff=0)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

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

if __name__ == '__main__':
    main() 
