# binding events with an event handler

from tkinter import *

class Application(Frame):
    """ GUI which counts button clicks """
    def __init__(self, master):
        """ Create Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        """ Create button """
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """ Count clicks """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

# main

root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()
        