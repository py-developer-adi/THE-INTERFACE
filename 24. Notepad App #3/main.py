'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *
from tkinter import simpledialog

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
    filename = simpledialog.askstring(
        "Filename",
        "Enter the filename to save: "
    )
    data = text.get(1.0, END)
    
    with open(
        f"{filename}.txt", "w"
    ) as f:
        f.write(data)
    
# & Open File Function
def open_file():
    '''this fun
    ction will open a file'''
    filename = simpledialog.askstring(
        "Filename",
        "Enter the filename to open: "
    )
    
    with open(f"{filename}.txt") as f:
        new_file()
        # create a new file to clear previous data
        text.insert(1.0, f.read())
    
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