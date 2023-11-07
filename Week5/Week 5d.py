# Event binding II (Mouse move)

import tkinter as tk
from tkinter import ttk


def click_event(event):
    if event.num == 1:
        button = "Left"
    elif event.num == 2:
        button = "Middle"
    else:
        button = "Right"

    message = button + " clicked to " + event.widget["text"]

    ttk.Label(win, text=message).pack()


def mouse_enter(event):
    # event.widget["text"] = "Mouse entered"
    event.widget.configure(text="Mouse entered")


def mouse_leave(event):
    event.widget["text"] = "Mouse left"


def mouse_move(event):
    win.title(f"{event.x}, {event.y}")


win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")
win.geometry("300x300+500+200")

btn1 = ttk.Button(win, text="Button 1")
btn2 = ttk.Button(win, text="Button 2")

btn1.pack(pady=(20, 0))
btn2.pack(pady=20)

btn1.bind("<Button-1>", click_event)  # Double-Button-1, ButtonRelease-1
btn2.bind("<Button-3>", click_event)
btn1.bind("<Enter>", mouse_enter)
btn1.bind("<Leave>", mouse_leave)
win.bind("<Motion>", mouse_move)  # B1-Motion, B3-Motion

btn1.focus()

win.mainloop()
