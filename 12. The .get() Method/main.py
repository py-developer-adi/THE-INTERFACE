'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

# ! Root Window
root = tk.Tk()
root.title(".get() Method | PyCODE")
root.geometry("600x300")

# * Function
def get_ent():
    '''This function will get the input given by user'''
    print(ent.get())

# & Entry
ent = tk.Entry(root)
ent.pack()

tk.Button(
    root, text="Get",
    command=get_ent
).pack()

# ! Running the UI
root.mainloop()