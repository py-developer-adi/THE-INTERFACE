'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

# ! Root Window
root = tk.Tk()
root.geometry("600x400")
root.title("Layouts | PyCODE")

# | side ["left", "right", "top", "bottom"]
# | anchor ["n", "s", "e", "w", "nw", "ne", "sw", "se", "center"]

tk.Label(
    root, text="Hello world"
).pack(anchor="nw")

# ! Running the UI
root.mainloop()