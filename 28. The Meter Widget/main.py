'''PyCODE | @_py.code'''

# ? Importing Libraries
from ttkbootstrap import *

# ! THE ROOT WINDOW
root = Window(themename='minty')
root.geometry("600x400")
root.title("Meter Widget | PyCODE")

# | A Meter
meter = Meter(
    root, amounttotal=350, amountused=250, textright="Km/h", bootstyle="danger", stripethickness=5, metertype="semi"
)
meter.pack()

# ! RUN THE UI
root.mainloop()