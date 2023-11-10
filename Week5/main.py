import tkinter as tk
from tkinter import ttk


def configure():
    print("asdasd")
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfigure("window", width=canvas.winfo_width())


def add():
    for i in range(0, 25):
        label.append(ttk.Label(frame, text=f"{len(label)}"))
        label[-1].pack()
    canvas.update()
    configure()


label = []

window = tk.Tk()

window.title("Main App")

window.geometry("600x400")
frameL = ttk.Frame(window)
frameL.pack(
    side="left",
)
# Add a container frame for the canvas and scrollbar widgets
container = tk.Frame(window)
container.pack(fill="both", expand=True)

# Add a canvas widget that will create a scrollable area
canvas = tk.Canvas(container)
canvas.pack(fill="both", expand=True)

# Add a scrollbar widget
sb = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

# Configure the canvas to respond to y-axis scrolling commands
canvas.configure(yscrollcommand=sb.set)
frame = ttk.Frame(canvas)
frame.pack(fill="both", expand=True)

# Configure the canvas to respond to y-axis scrolling commands
canvas.configure(yscrollcommand=sb.set)

canvas.create_window((0, 0), window=frame, tags="window", anchor="ne")
sb.place(relx=1, rely=0, relheight=1, anchor="ne")

canvas.bind("<Configure>", lambda event: configure())

ttk.Button(master=frameL, text="Click", command=add).pack(
    anchor="center", fill="both", expand=True
)
window.mainloop()
