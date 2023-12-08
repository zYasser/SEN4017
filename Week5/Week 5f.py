# Context menu

import tkinter as tk
from tkinter import ttk
from datetime import datetime


def show_context_menu(event):
    # Places the context menu to the (x,y) coordinate of the mouse.
    # x_root, y_root returns the coordinate of the mouse relative to the top left corner of the screen.
    # x, y returns the coordinate of the mouse relative to the top left corner of the widget.
    context_menu.tk_popup(x=event.x_root, y=event.y_root)


def show_date():
    # ttk.Label(win, text=str(datetime.now()), font=("Consolas", 16)).pack(pady=(10, 0))
    labels.append(ttk.Label(win, text=datetime.now().strftime("%d.%m.%Y - %H:%M:%S"), font=("Consolas", 16)))
    labels[-1].pack(pady=(10, 0))


def clear():
    for label in labels:
        label.destroy()
    labels.clear()


win = tk.Tk()
win.title("SEN4017 - Week 5")
win.geometry("300x300+500+200")
labels = []

context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date)
context_menu.add_command(label="Clear", command=clear)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)

win.bind("<Button-3>", show_context_menu)

win.mainloop()
