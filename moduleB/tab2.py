import tkinter as tk
from tkinter import ttk


class Tab(tk.Tk):
    def __init__(self, page2):
        self.state = 0
        
        def start():
            print("start")
        
        button_start = tk.Button(page2, text="Start", command=start, width=10, height=1)
        button_stop = tk.Button(page2, text="Start", command=start, width=10, height=1)
        button_snap = tk.Button(page2, text="Start", command=start, width=10, height=1)
        button_unsnap = tk.Button(page2, text="Start", command=start, width=10, height=1)

        button_start.grid(row=0, column=0, padx=10, pady=10, sticky="NW")
        button_stop.grid(row=0, column=1, padx=10, pady=10, sticky="NE")
        button_snap.grid(row=0, column=2, padx=10, pady=10, sticky="NW")
        button_unsnap.grid(row=0, column=3, padx=10, pady=10, sticky="NE")