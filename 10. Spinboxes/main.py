'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

# ! Root Window
root = tk.Tk()
root.title("Spinboxes | PyCODE")
root.geometry("600x300")

# & Spinbox
num = tk.Spinbox(root)
num.pack()

# | from_=<value>
# | to=<value>
num.config(to = 100)
num.config(from_ = 1)

# | value=<value>
num.config(value=5)

# & Custom Spinbox
custom = tk.Spinbox(root)
custom.pack()

# | Custom Values
custom.config(values=[
    "Option 1",
    "Option 2",
    "Option 3"
])

# ! Running the UI
root.mainloop()