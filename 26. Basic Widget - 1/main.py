'''PyCODE | @_py.code'''

# ? Importing Libraries
from ttkbootstrap import *

# ! THE ROOT WINDOW
root = Window(themename="minty")
root.geometry("600x400")
root.title("Basic Widgets | PyCODE")

# | Label
Label(
    root, text="Hello",
    style="danger"
).pack()

# | Entry
Entry(
    root, style="success"
).pack()

# | Button
Button(
    root, text="Click",
    style="info"
).pack()

# ! RUN THE UI
root.mainloop()

# | https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/
# | https://ttkbootstrap.readthedocs.io/en/latest/styleguide/meter/