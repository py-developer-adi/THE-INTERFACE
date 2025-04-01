'''PyCODE | @_py.code'''

# $ pip install ttkbootstrap

# ? Importing Libraries
from ttkbootstrap import *

# ! THE ROOT WINDOW
root = Window(
    themename="darkly"
)
root.title(
    "TTKBOOTSTRAP | PyCODE"
)
root.geometry(
    "600x400"
)

# ! RUN THE UI
root.mainloop()