import tkinter as tk

win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

label1.pack(ipadx=10, ipady=10, fill="y", expand=True)  # x, y, both
label2.pack(ipadx=10, ipady=10, anchor="w")  # n, s, w, e, ...
label3.pack(ipadx=10, ipady=10, anchor="e")

win.mainloop()
