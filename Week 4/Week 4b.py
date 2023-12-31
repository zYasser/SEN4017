# Menu with accelerators and underline

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+100+100")

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0)
file_menu.add_command(label="Open...", underline=0)  # underline specifies the character index (press <Alt> for Windows)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.destroy, underline=1)

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_command(label="About...")

menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu)

win.mainloop()
