# Center screen

import tkinter as tk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")

# Define the window's width and height
win_width = 600
win_height = 800

# Find the screen's width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the window's top left corner position
x = int((screen_width / 2) - (win_width / 2))
y = int((screen_height / 2) - (win_height / 2))

# Place the window
win.geometry(f"{win_width}x{win_height}+{x}+{y}")

print(f"Screen resolution: {screen_width}x{screen_height}")

win.mainloop()
