# Scrollable frame

import tkinter as tk
from tkinter import ttk
from datetime import datetime


def show_context_menu(event):
    # Places the context menu to the (x,y) coordinate of the mouse.
    # x_root, y_root returns the coordinate of the mouse relative to the top left corner of the screen.
    # x, y returns the coordinate of the mouse relative to the top left corner of the widget.
    context_menu.tk_popup(x=event.x_root, y=event.y_root)


def show_date():
    labels.append(
        ttk.Label(
            content,
            text=datetime.now().strftime("%d.%m.%Y - %H:%M:%S"),
            font=("Consolas", 16),
        )
    )
    labels[-1].pack(pady=10)
    canvas.update()  # Refresh the canvas GUI after adding a new label
    configure_canvas()


def clear():
    for label in labels:
        label.destroy()
    labels.clear()


def configure_canvas():
    print(canvas.bbox("all"))
    canvas.configure(scrollregion=canvas.bbox("all"))
    # # Adjust the content frame (content_window) width to match the width of the canvas
    canvas.itemconfigure("content_window", width=canvas.winfo_width())


def configure_canvas_event(event):
    configure_canvas()


win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")
win.geometry("300x300+500+200")
labels = []
# frameL = ttk.Frame(win)
# frameL.pack(
#     side="left",
# )
# ttk.Button(master=frameL, text="Click").pack(anchor="center", fill="both", expand=True)

# Add a container frame for the canvas and scrollbar widgets
container = tk.Frame(win)
container.pack(fill="both", expand=True)

# Add a canvas widget that will create a scrollable area
canvas = tk.Canvas(container)
canvas.pack(fill="both", expand=True)

# Add a scrollbar widget
sb = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

# Configure the canvas to respond to y-axis scrolling commands
canvas.configure(yscrollcommand=sb.set)

# Create a frame that will keep the actual content
content = tk.Frame(canvas)
content.pack(fill="both", expand=True)
sb.place(relx=1, rely=0, relheight=1, anchor="ne")

# Add the content frame to the canvas widget
canvas.create_window((0, 0), window=content, anchor="ne", tags="content_window")

# Adjust the canvas width and scrollable area
canvas.bind("<Configure>", configure_canvas_event)

# Add a context menu to the content frame
context_menu = tk.Menu(content, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date)
context_menu.add_command(label="Clear", command=clear)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)

# Bind the context menu to the right mouse button click event
win.bind("<Button-3>", show_context_menu)

win.mainloop()
