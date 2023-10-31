import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SEN4017")
win.geometry("300x200+100+100")
# win.resizable(False, False)
ttk.Label(win, text="A label").grid(column=0, row=0)
win.mainloop()
