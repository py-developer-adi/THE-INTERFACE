'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *
from tkinter.filedialog import askopenfilename

# ! THE ROOT WINDOW
root = Tk()
root.title("Pop-up File Manager | PyCODE")
root.geometry("600x400")

filename = askopenfilename(
    filetypes=[
    ("Python Files", "*.py"),
    ("JavaScript Files", "*.js"),
    ("Text Files", "*.txt"),
    ("All Files", "*.*")
]
)

if filename:
    with open(filename) as f:
        print(f.read())

# ! RUN THE UI
root.mainloop()

# | Notepad app part 3??