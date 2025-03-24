'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *
from tkinter import messagebox

# ! THE ROOT WINDOW
root = Tk()
root.title("Messagebox | PyCODE")
root.geometry("600x400")

# & Function to pop-up message
def show_msg(
    title, message
):
    '''pop-ups the message'''
    messagebox.showinfo(
        title,
        message
    )

# & Function to show error
def err_msg(
    title,
    message
):
    messagebox.showerror(
        title,
        message
    )
    
# & Function to show warning
def warn_msg(
    title,
    message
):
    messagebox.showwarning(
        title,
        message
    )
    
show_msg("Hi", "some info")
err_msg("Hi", "some error")
warn_msg("Hi", "some warning")

# ! RUN THE UI
root.mainloop()