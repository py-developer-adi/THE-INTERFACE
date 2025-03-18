'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

# ! Root Window
root = tk.Tk()
root.title("Grids & Place | PyCODE")
root.geometry("600x400")

# | THE GRID LAYOUT
l1 = tk.Label(
    root, text="Python"
)
l2 = tk.Label(
    root, text="UI"
)
l3 = tk.Label(
    root, text="Tkinter"
)

l1.grid(row=0, column=0, sticky="w")
l2.grid(row=0, column=1, sticky="w")
l3.grid(row=1, column=1, sticky="w")

# | THE PLACE LAYOUT
l1 = tk.Label(
    root, text="Place"
)
l2 = tk.Label(
    root, text="Layout"
)
l3 = tk.Label(
    root, text="(x, y)"
)

l1.place(x=45, y=85)
l2.place(x=235, y=45)
l3.place(x=45, y=105)

# ! Running the UI
root.mainloop()