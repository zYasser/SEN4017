import tkinter as tk

win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("300x300+100+100")
label1 = tk.Label(win, text="Enter your name:")
label2 = tk.Label(win, text="")
entry1 = tk.Entry(win, width=30)


def click_handler():
    label2.configure(text="Hello " + entry1.get())


button1 = tk.Button(win, text="Send", command=click_handler)  # state="disabled"

label1.pack()
entry1.pack()
button1.pack()
label2.pack()

win.mainloop()
