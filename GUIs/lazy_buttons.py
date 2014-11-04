# buttons

from tkinter import *

root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

# frame
app = Frame(root)
app.grid()

# button

bttn1 = Button(app, text = "ME SO BUTTONY!")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "ME TOO!")


bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Same Here"

root.mainloop()
