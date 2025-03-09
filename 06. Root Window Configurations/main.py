'''PyCODE | @_py.code'''
# | 06. Root Window Configurations

# ? Importing Libraries
from tkinter import *

width = 800
height = 500

# ! Main Window
root = Tk()

root.title("My UI")
root.geometry(
    f"{width}x{height}"
)

# & root.resizable(width, height)
root.resizable(True, False)

# & root.maxsize(width, height)
# & root.minsize(width, height)
root.maxsize(1000, 1000)
root.minsize(100, 200)

# & root.iconbitmap('your_icon.ico')
root.iconbitmap('icon.ico')

# & root.config(bg='color')
root.config(bg='#7e9be3')

# ? Run the UI
root.mainloop()