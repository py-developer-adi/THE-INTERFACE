'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

root = tk.Tk()
root.geometry("600x300")
root.title("07. Widgets I")

# & tk.Label(where_to_pack, text).pack()

text1 = tk.Label(root, text="Hello World")
text1.pack()

# & entry = tk.Entry(where_to_pack)
# & .pack()

entry = tk.Entry(root)
entry.pack()

# & tk.Button(where_to_pack, text).pack()

btn = tk.Button(root, text="Click Me")
btn.pack()

root.mainloop()