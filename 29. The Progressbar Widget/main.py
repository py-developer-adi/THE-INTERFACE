'''PyCODE | @_py.code'''

# ? Importing Libraries
from ttkbootstrap import *
import time

# ! THE ROOT WINDOW
root = Window(themename="minty")
root.geometry("600x400")
root.title("The Progressbar Widge t | PyCODE")

def move(bar: Progressbar):
    current_value = bar.cget("value")
    if current_value < bar.cget("maximum"):
        bar.config(value=current_value + 1)
        root.after(5, move, bar)  # Adjust speed by changing the milliseconds
    else:
        bar.config(value=0)
        root.after(5, move, bar)  # Restart after short pause
    

# | Progressbar
bar1 = Progressbar(
    root, maximum=150, value=100, style="success-striped", orient="horizontal",
    mode="determinate"
)
bar1.pack(padx=10, pady=10)

# Get Value
# //print(bar.cget("value"))

# Set Value
# //bar.config(value=140)

bar2 = Progressbar(
    root, maximum=150, value=100, style="danger", orient="horizontal",
    mode="indeterminate"
)
bar2.pack(padx=10, pady=10)

move(bar=bar1)
move(bar=bar2)

# ! RUN THE UI
root.mainloop()