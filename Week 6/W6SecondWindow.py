import tkinter as tk
from tkinter import ttk


class SecondWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Second Window")
        self.geometry("300x200")
        self.lbl1 = None
        self.entry1 = None
        self.btn1 = None
        self.create_widgets()

        # Define the behavior of a window when the user attempts to close it
        # by clicking the "X" button in the window's title bar
        # self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        self.lbl1 = ttk.Label(self, text="Second Window", font=("Calibri", 16))
        self.lbl1.pack(pady=(20, 0))

        self.entry1 = ttk.Entry(self)
        self.entry1.pack(pady=(20, 0))
        self.entry1.bind("<Return>", self.return_key)

        self.btn1 = ttk.Button(self, text="Close", command=self.close_window)
        self.btn1.pack(pady=(20, 0))

    def return_key(self, event):
        self.parent.win.title(self.entry1.get())  # Change the parent window's title
        self.close_window()

    def close_window(self):
        print("Closing the second window.")
        self.destroy()
