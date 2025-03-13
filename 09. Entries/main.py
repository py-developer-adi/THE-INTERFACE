'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

# ! Root window
root = tk.Tk()
root.geometry("600x400")
root.title("Entries | PyCODE")

# & Simple Entry
user = tk.Entry(root)
user.pack()

# | Customzed Entry
custom = tk.Entry(root, show="|")
custom.pack()

# | Placeholders
user.insert(0, "Enter your name")

root.mainloop()