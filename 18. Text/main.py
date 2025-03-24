'''PyCODE | @_py.code'''

# ? Importing Libraries
from tkinter import *

# ! The Root Window
root = Tk()
root.title("Text | PyCODE")
root.geometry("600x400")

# ? Getting the text of Text widget
def get_text():
    # // get(str, end)
    text_content = text.get(
        "1.0", END
    )
    print(text_content)
    
# ? Inserting Text
def add():
    # // insert(index, text)
    text.insert(
        END, "Hello, World!"
    )

# | Text Widget
text = Text(root)
text.grid(row=0, column=0)

add()

# ! Run the UI
root.mainloop()