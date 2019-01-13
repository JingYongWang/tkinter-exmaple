import tkinter as tk
from tkinter import ttk

import moduleA.tab1 as tab1
import moduleB.tab2 as tab2
class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('800x400')
        self.title = "NoteBook"
    

        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows += 1

        nb = ttk.Notebook(self)
        nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="NEWS")

        page1 = ttk.Frame(nb)
        nb.add(page1, text="Tab1")
        tab1.Tab(page1)

        page2 = ttk.Frame(nb)
        nb.add(page2, text="Tab2")
        tab2.Tab(page2)

        self.mainloop()

if __name__ == "__main__":
    main = Main()
    main.mainloop()


try:    # python 2.x
    from Tkinter import *
    import ttk

except ImportError:
    # python
    from tkinter import *
    from tkinter import ttk

