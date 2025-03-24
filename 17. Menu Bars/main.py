'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *

# ! The Root Window
root = Tk()
root.geometry("600x400")
root.title("Menu | PyCODE")

# | Bidning Function with the menu
def func():
    print("Doing something...")

# | Creating Menu
menu = Menu(root)

# | Adding Commands
menu.add_command(
    label="Hello",
    command=func
)

# | Advanced Menu
submenu = Menu(menu)
submenu.add_command(label="Func1")
submenu.add_command(label="Func2")
submenu.add_separator()
submenu.add_command(label="Func3")

menu.add_cascade(label="Advanced", menu=submenu)

# ! Run the UI
root.config(menu=menu)
root.mainloop()