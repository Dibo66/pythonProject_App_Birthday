from tkinter import *


class MyButton(Button):
    def __init__(self,master,**kwargs):
        super().__init__(master=master, **kwargs)
        self.my_buttons = {"font":"Sans 12 bold", "width":12}
        self.config(self.my_buttons)


class appButton(Button):
    def __init__(self,master,**kwargs):
        super().__init__(master=master, **kwargs)
        self.app_buttons = {"font": "arial 12 bold", "fg": "#42bcf5", "bg": "white"}
        self.config(self.app_buttons)

