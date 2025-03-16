'''PyCODE | @_py.code'''

# ? Importing Libraries
import tkinter as tk

# ! Root Window
root = tk.Tk()
root.geometry("600x300")
root.title("Buttons | PyCODE")

# & Creating Buttons
btn = tk.Button(
    root, text="Click"
)
btn.pack()

# | Button Command
def start():
    """Called when the button is clicked"""
    print("Clicked!")
    
# : Bind func to btn
btn.config(
    command=start
)

# & Disabling Buttons
btn2 = tk.Button(
    root, text="Click",
    state='disabled'
)
btn2.pack()

# ! Running the UI
root.mainloop()