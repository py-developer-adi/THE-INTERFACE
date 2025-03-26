'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *

# ! The Root Window
root = Tk()
root.title("Notepad | PyCODE")
root.geometry("600x400")

# & New File Function
def new_file():
    '''this function will clear the text area'''
    # // .delete(st, end)
    text.delete(1.0, END)
    
# & Save File Function
def save_file():
    '''this function will save the file'''

# & Open File Function
def open_file():
    '''this fun
    ction will open a file'''
    
# | Menu
menu = Menu(root)
menu.add_command(
    label="New File",
    command=new_file
)
menu.add_command(
    label="Open File",
    command=open_file
)
menu.add_command(
    label="Save File",
    command=save_file
)

# | Text Area
text = Text(root)
text.grid(row=0, column=0, sticky="nsew")

# ! Root Configs
root.config(menu=menu) 

# ! Run the UI 
root.mainloop()

# | Source code at github.
