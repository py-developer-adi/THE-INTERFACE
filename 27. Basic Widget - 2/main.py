'''PyCODE | @_py.code'''

# ? Importing Libraries
from ttkbootstrap import *

# ! THE ROOT WINDOW
root = Window(themename="minty")
root.geometry("600x400")
root.title("Basic Widgets | PyCODE")

def func():
    print(
        date.entry.get()
    )

# | DateEntry
date = DateEntry(
    root, bootstyle="success",
    dateformat="%d:%m-%Y",
    firstweekday=0
)
date.pack()

btn = Button(
    root, text="GET", style="success",
    command=func
)
btn.pack()

# ! RUN THE UI
root.mainloop()