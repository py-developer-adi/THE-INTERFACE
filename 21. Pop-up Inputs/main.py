'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *
from tkinter import simpledialog

# ! THE ROOT WINDOW
root = Tk()
root.title("Pop-up Inputs | PyCODE")
root.geometry("600x400")

string = simpledialog.askstring(
    "Name", "Enter your name"
)

integer = simpledialog.askinteger(
    "Title", "Prompt"
)

fl = simpledialog.askfloat(
    "Float", "Enter a float value"
)

simpledialog.askstring(
    "title", "prompt",
    initialvalue="Name", show="*"
)

print(string)
print(integer)
print(fl)

# | source code at github

# ! RUN THE UI
root.mainloop()