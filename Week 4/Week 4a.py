# Simple menu

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+100+100")
win.iconbitmap("python.ico")

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Exit", command=win.destroy)

menubar.add_cascade(label="File", menu=file_menu, underline=0)

win.mainloop()
