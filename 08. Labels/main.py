'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

# ! Root Window
root = tk.Tk()
root.geometry("400x200")
root.title("Labels | PyCODE")

# & Creating a Label
text = tk.Label(
    root,
    text="Hello World"
)
text.pack()

# & Displaying Image
image = tk.PhotoImage(
    file='image.png'
)
img = tk.Label(
    root,
    image=image
)
img.pack()

# ! Running the Window
root.mainloop()