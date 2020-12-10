from tkinter import *
import datetime
from testappMypeople import MyPeople
from testappAddpeople import AddPeople
from testappAboutus import About
import query_in_functions

ddate = datetime.date.today()
date = str(ddate)

# add comment here


class Application(object):
    def __init__(self, master):
        self.master = master

        # frame
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#3252a8')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_lable = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lable.place(x=130, y=20)

        self.heading = Label(self.top, text='My phone book', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=230, y=50)

        self.date_lbl = Label(self.top, text="Today's date:" + date, font='arial 12 bold', fg='#ebb434', bg='white')
        self.date_lbl.place(x=450, y=110)

        bd_persons = str(len(query_in_functions.bday_persons()))
        self.bd_lbl = Label(self.top, text=f"Birthday today: {bd_persons}", font='arial 12 bold', fg='#ebb434', bg='white')
        self.bd_lbl.place(x=40, y=110)
        #===============================

        # button1 peoples
        self.viewButton = Button(self.bottom, text="  My People  ", fg="#42bcf5", bg="white"
                                 , font='arial 12 bold', command=self.my_people)
        self.viewButton.place(x=250, y=70)

        # button2 add people
        self.addButton = Button(self.bottom, text=" Add People ", fg="#42bcf5", bg="white", font='arial 12 bold',
                                command=self.addpeoplefunction)
        self.addButton.place(x=250, y=130)

        # button3 about
        self.aboutButton = Button(self.bottom, text="   About Us   ", fg="#42bcf5", bg="white", font='arial 12 bold',
                                  command=self.about_us)
        self.aboutButton.place(x=250, y=190)

        # button4 refresh
        self.aboutButton = Button(self.bottom, text="    Refresh     ", fg="#42bcf5", bg="white", font='arial 12 bold',
                                  command=self.refresh_bd_label)
        self.aboutButton.place(x=250, y=250)

    def my_people(self):
        people = MyPeople()

    def about_us(self):
        aboutpage = About()

    def addpeoplefunction(self):
        addpeoplewindow = AddPeople()

#=============================
    def refresh_bd_label(self):
        bd_persons = str(len(query_in_functions.bday_persons()))
        self.bd_lbl.config(text=f"Birthday today: {bd_persons}")
#===========================


def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry("650x550+350+200")
    root.resizable(False, False)

    root.mainloop()


if __name__ == "__main__":
    main()
