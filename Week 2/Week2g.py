import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SEN4017")
win.geometry("300x200+100+100")
# win.resizable(False, False)
label1 = ttk.Label(win, text="A label")
label1.grid(column=0, row=0)


def click_handler():
    button1.configure(text="** User clicked **")
    label1.configure(foreground="red")
    label1.configure(text="A red label")


button1 = ttk.Button(win, text="A button", command=click_handler)
button1.grid(column=1, row=0)
win.mainloop()
