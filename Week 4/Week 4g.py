# Spinbox

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+100+100")


def click_handler():
    ttk.Label(win, text=spin_value.get()).pack()


spin_value = tk.StringVar()
spin_values = tuple(range(1, 20, 3))
# spinbox1 = ttk.Spinbox(win, from_=0, to=10, wrap=True, state="readonly", textvariable=spin_value)
spinbox1 = ttk.Spinbox(win, values=(1, 3, 5, 7), wrap=True, textvariable=spin_value)
# spinbox1 = ttk.Spinbox(win, values=spin_values, wrap=True, textvariable=spin_value)
# spinbox1 = ttk.Spinbox(
#     win, values=spin_values, wrap=True, textvariable=spin_value, command=click_handler
# )

spinbox1.pack()

win.mainloop()
