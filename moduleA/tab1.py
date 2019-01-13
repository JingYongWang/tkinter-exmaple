import tkinter as tk
from tkinter import ttk

import subprocess 



class Tab(tk.Tk):
    def __init__(self, page1):
        self.state = 0

        def state():
            print("Test State FUn")

        def start():
            print("start")
            button_stop.config(state="normal")
            button_snap.config(state="normal")
            process = subprocess.Popen("python sleep.py", cwd="./cmd", shell=True)
            if process.wait() == 0:
                print("process success")
            else:
                print("Fail")
            # button_stop.config(tk.NORMAL)
            # button_stop.config(state="normal")

        def stop():
            print("stop")
            button_stop.config(state="normal")     

        def snap():
            print("snap")
            button_stop.config(state="normal")     

        def unsnap():
            print("unsnap")
            button_stop.config(state="normal") 
            button_snap.config(state="normal")     

        def unlock(event):
            print("unsnap")
            button_stop.config(state="disabled") 
            button_snap.config(state="disabled")   
   
        button_start = tk.Button(page1, text="Start", command=start, width=10, height=1)
        button_stop = tk.Button(page1, text="Start", command=stop, width=10, height=1)
        button_snap = tk.Button(page1, text="Start", command=snap, width=10, height=1)
        button_unsnap = tk.Button(page1, text="Start", command=unsnap, width=10, height=1)
        button_start.bind("<Button-1>", unlock)
       

        button_start.grid(row=0, column=0, padx=10, pady=10, sticky="NW")
        button_stop.grid(row=0, column=1, padx=10, pady=10, sticky="NE")
        button_snap.grid(row=0, column=2, padx=10, pady=10, sticky="NW")
        button_unsnap.grid(row=0, column=3, padx=10, pady=10, sticky="NE")
