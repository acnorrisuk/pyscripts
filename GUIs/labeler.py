# demonstrates labels

from tkinter import *

# create root window
root = Tk()
root.title("Labeler")
root.geometry("200x50")

# frame to hold widgets

app = Frame(root)
# layout
app.grid()

# create label

lbl = Label(app, text = "Labelman!")
lbl.grid()

root.mainloop()
