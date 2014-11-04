# using classes

from tkinter import *

class Application(Frame):
    """ A GUI APP with 3 buttons """
    def __init__(self, master):
        """ Create Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = Button(self, text = "Rubbish")
        self.bttn1.grid()
        
        self.bttn2 = Button(self, text = "Poo!")
        self.bttn2.grid()
        
        self.bttn3 = Button(self, text = "Pants")
        self.bttn3.grid()

# main
root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")

app = Application(root)

root.mainloop()
