# Center screen - with function.

import tkinter as tk
from centerscreen import center_screen_geometry

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")

# Call the "center_screen_geometry" function from centerscreen.py
win.geometry(center_screen_geometry(screen_width=win.winfo_screenwidth(),
                                    screen_height=win.winfo_screenheight(),
                                    window_width=300,
                                    window_height=300))

win.mainloop()
