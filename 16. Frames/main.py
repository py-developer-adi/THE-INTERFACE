'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *

# ! The Root Window
root = Tk()
root.title("Frames | PyCODE")
root.geometry("600x400")

# | A Frame
frame = Frame(
    root,
    width=100, height=100,
    bg="#c3c3c3",
    padx=5, pady=5
)
frame.grid(row=0, column=0)

# & The #c3c3c3 is hex color code that will give gray color to the Frame

# | Adding widgets to Frame
Label(
    frame, text="Hello World"
).grid(row=0, column=0)

# : Next - Menu Bars



# ! Run the UI
root.mainloop()