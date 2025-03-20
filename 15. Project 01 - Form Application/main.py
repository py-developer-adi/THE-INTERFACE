'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *

# ! Root Window
root = Tk()
root.title("Form Application - PyCODE")
root.geometry("600x400")

# * Function for Form Submission
def submit():
    name_v = name.get()
    email_v = email.get()
    password_v = password.get()
    
    with open(
        f"{email_v}.txt", "w"
    ) as f:
        f.write(name_v + '\n')
        f.write(email_v + '\n')
        f.write(password_v + '\n')

# | Headline
Label(
    root,
    text="Form Application",
    font=("", 20, "bold")
).grid(
    row=0, column=0,
    columnspan=2
)

# & The font attribute is used to give customized font to a Widget.

# | Name
Label(
    root, text="Your Name"
).grid(
    row=1, column=0,
    sticky="w"
)

name = Entry(root)
name.grid(
    row=1, column=1,
    sticky="w"
)

# | Email
Label(
    root, text="Your Email"
).grid(
    row=2, column=0,
    sticky="w"
)

email = Entry(root)
email.grid(
    row=2, column=1,
    sticky="w"
)

# | Password
Label(
    root, text="Your Password"
).grid(
    row=3, column=0,
    sticky="w"
)

password = Entry(root)
password.grid(
    row=3, column=1,
    sticky="w"
)

# | Button
Button(
    root, text="Submit",
    command=submit
).grid(
    row=4, column=1,
    columnspan=2
)

# : columnspan is used to merge two columns for a widget

# : font('font_name', size, 'weight') is used to give cusomized font

# ! Run the UI
root.mainloop()